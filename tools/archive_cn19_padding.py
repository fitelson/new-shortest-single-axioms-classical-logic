#!/usr/bin/env python3
"""Statically recover CN19 evidence from the preserved padded CN21 records.

Copies existing results only; never enumerates candidates or invokes a prover.
Usage: python3 tools/archive_cn19_padding.py /path/to/walsh_meredith
"""
import argparse
import csv
import gzip
import hashlib
import json
from pathlib import Path
import re
import shutil

import candidate_index as ci


def digest(path):
    h = hashlib.sha256()
    with path.open('rb') as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b''):
            h.update(block)
    return h.hexdigest()


def fresh_padding(formula):
    return (len(formula) == 21 and formula[0] == 'C' and
            formula[1].isdigit() and formula[1] not in formula[2:])


def renumber(formula):
    names = {}
    result = []
    for c in formula:
        if c.isdigit():
            names.setdefault(c, str(len(names)))
            c = names[c]
        result.append(c)
    return ''.join(result)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('project', type=Path)
    args = parser.parse_args()
    project = args.project.resolve()
    source_root = project / 'code/legacy_walsh_search/Results/CN21Results'
    named = json.loads((ci.ROOT / 'named_candidates.json').read_text())
    by_formula = {r['legacy_polish']: r for r in named if r['system'] == 'CD_CN' and r['weight'] == 19}
    old_list = source_root / 'specialcases/CN_21_Remaining.txt'
    output_root = ci.ROOT / 'evidence/CN19_padding'
    output_root.mkdir(parents=True, exist_ok=True)
    mappings = []
    for line_number, text in enumerate(old_list.read_text().splitlines(), 1):
        formula = text.strip()
        if not fresh_padding(formula):
            continue
        stripped = renumber(formula[2:])
        row = {'id': f'CN19_padding_{line_number:04d}',
               'legacy_survivor_line': line_number, 'padded': formula,
               'stripped_legacy_polish': stripped}
        output = source_root / 'specialcases' / (formula + '.out')
        if output.is_file():
            contents = output.read_text()
            assert 'SZS status CounterSatisfiable' in contents, output
            destination = output_root / output.name
            if destination.exists():
                assert destination.read_bytes() == output.read_bytes(), destination
            else:
                shutil.copyfile(output, destination)
            row.update(method='finite model' if 'output start FiniteModel' in contents else 'completed saturation',
                       evidence=str(destination.relative_to(ci.REPO)),
                       vampire_versions=sorted(set(re.findall(r'Version:\s*([^\n]+)', contents))),
                       output_sha256=digest(destination))
        else:
            match = by_formula[stripped]
            row.update(method='see named candidate', named_candidate=match['id'],
                       evidence=match['evidence'])
        mappings.append(row)
    assert len(mappings) == 77
    assert sum('output_sha256' in r for r in mappings) == 59
    by_padded = {r['padded']: r for r in mappings}
    source = source_root / 'CN_21_CounterModels.txt'
    destination = ci.ROOT / 'legacy/CD_CN19_from_CN21.tsv.gz'
    h = hashlib.sha256()
    selected = models = source_rows = 0
    exceptions = []
    with source.open('rb') as stream, destination.open('wb') as output:
        with gzip.GzipFile(filename='', fileobj=output, mode='wb', mtime=0, compresslevel=6) as zipped:
            zipped.write(b'legacy_polish\tpadded_legacy_polish\tsource_line\tmethod\tcompact_countermodel\tevidence_id\n')
            for source_rows, raw in enumerate(stream, 1):
                h.update(raw)
                text = raw.decode().strip()
                formula, _, model = text.partition(':')
                if fresh_padding(formula):
                    assert 'NN' not in formula, formula
                    selected += 1
                    stripped = renumber(formula[2:])
                    if model:
                        models += 1
                        method, evidence_id = 'finite countermodel', ''
                    else:
                        mapped = by_padded[formula]
                        evidence_id = mapped['id']
                        method = 'see padding exception map'
                        exceptions.append({'line': source_rows, 'formula': formula, 'id': evidence_id})
                    zipped.write(f'{stripped}\t{formula}\t{source_rows}\t{method}\t{model}\t{evidence_id}\n'.encode())
                if source_rows % 5000000 == 0:
                    print(f'Read {source_rows:,} legacy rows; copied {selected:,} padded rows.', flush=True)
    assert len(exceptions) == 77
    assert {r['formula'] for r in exceptions} == set(by_padded)
    mapping_path = ci.ROOT / 'cn19_padding_exceptions.json'
    mapping_path.write_text(json.dumps(mappings, indent=2) + '\n')
    with (ci.ROOT / 'cn19_padding_exceptions.tsv').open('w') as stream:
        writer = csv.writer(stream, delimiter='\t', lineterminator='\n')
        writer.writerow(('id', 'padded', 'stripped_legacy_polish', 'method', 'named_candidate', 'evidence', 'vampire_versions'))
        for r in mappings:
            writer.writerow((r['id'], r['padded'], r['stripped_legacy_polish'], r['method'],
                             r.get('named_candidate', ''), r['evidence'], '; '.join(r.get('vampire_versions', []))))
    entry = {'dataset': 'CD_CN19_from_CN21', 'system': 'CD_CN', 'weight': 19,
             'padding_weight': 21, 'scope': 'DN-free; legacy variable identifications unrestricted',
             'file': str(destination.relative_to(ci.REPO)), 'file_sha256': digest(destination),
             'source': str(source.relative_to(project)), 'source_sha256': h.hexdigest(),
             'source_rows': source_rows, 'rows': selected, 'finite_model_rows': models,
             'exceptions': exceptions, 'exception_map': str(mapping_path.relative_to(ci.REPO)),
             'saved_successful_outputs': 59, 'named_candidate_links': 18,
             'verification_scope': 'Static extraction of recorded matrix assignments and successful outputs, not bulk matrix re-verification or a new search.'}
    manifest_path = ci.ROOT / 'legacy_manifest.json'
    manifest = json.loads(manifest_path.read_text())
    manifest = [r for r in manifest if r['dataset'] != entry['dataset']] + [entry]
    manifest_path.write_text(json.dumps(manifest, indent=2) + '\n')
    print(json.dumps({k: v for k, v in entry.items() if k != 'exceptions'}, indent=2), flush=True)


if __name__ == '__main__':
    main()
