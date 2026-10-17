#!/usr/bin/env python3
"""Small finite checks supporting the human transfer/lifting arguments.

No theorem prover, candidate-axiom enumeration, or model search is invoked.
"""
import importlib.util
import itertools
import json
from pathlib import Path
import sys

import candidate_index as ci


def patterns(t):
    yield ('hole', ()), [t]
    if ci.is_variable(t):
        return
    name, args = t
    if not args:
        yield t, []
    elif len(args) == 1:
        for p, holes in patterns(args[0]):
            yield (name, (p,)), holes
    else:
        for a, ha in patterns(args[0]):
            for b, hb in patterns(args[1]):
                yield (name, (a, b)), ha + hb


def partitions(items):
    if not items:
        yield []
        return
    first, *rest = items
    for p in partitions(rest):
        yield [[first]] + p
        for k in range(len(p)):
            yield p[:k] + [[first] + p[k]] + p[k+1:]


def generalizations(t):
    unique = {}
    for pattern, holes in patterns(t):
        groups = {}
        for k, h in enumerate(holes):
            groups.setdefault(h, []).append(k)
        for choices in itertools.product(*(list(partitions(g)) for g in groups.values())):
            labels = {}
            for p in choices:
                for block in p:
                    v = f'G{len(set(labels.values()))}'
                    for index in block:
                        labels[index] = v
            iterator = iter(range(len(holes)))
            def fill(p):
                if p == ('hole', ()):
                    return labels[next(iterator)], ()
                return p[0], tuple(fill(x) for x in p[1])
            g = fill(pattern)
            unique[ci.canonical(g)] = g
    return list(unique.values())


def vars_of(t):
    return {t[0]} if ci.is_variable(t) else set().union(*(vars_of(a) for a in t[1]))


def classical(t, valuation):
    name, args = t
    if ci.is_variable(t):
        return valuation[name]
    if name == 'f':
        return False
    if name == 'o':
        return True
    if name == 'n':
        return not classical(args[0], valuation)
    return not classical(args[0], valuation) or classical(args[1], valuation)


def tautology(t):
    variables = sorted(vars_of(t))
    return all(classical(t, dict(zip(variables, values)))
               for values in itertools.product((False, True), repeat=len(variables)))


def substitute(t, name, replacement):
    return replacement if t == (name, ()) else (t[0], tuple(substitute(a, name, replacement) for a in t[1]))


def verify():
    counts = {}
    for formula, system in [('CCCpqrCCrpCsp', 'CD_CO'), ('CCpqCCqrCpr', 'CD_CN'),
                            ('CpCqp', 'CD_CN'), ('CCCpqpp', 'CD_CN'), ('CFp', 'CD_CF'),
                            ('CCNppp', 'CD_CN'), ('CpCNpq', 'CD_CN'), ('Cpp', 'CD_CN'), ('o', 'CD_CO')]:
        t = ci.parse_polish(formula, system)
        gs = generalizations(t)
        assert tautology(t)
        assert not [g for g in gs if ci.canonical(g) != ci.canonical(t) and tautology(g)], formula
        counts[formula] = len(gs)
    bad = ci.parse_polish('CCpCCqrCsNrCCNtpCrt', 'CD_CN')
    valuation = dict(zip(('Vp', 'Vq', 'Vr', 'Vs', 'Vt'), (True, False, True, False, False)))
    assert not classical(bad, valuation)
    o4 = ci.parse_polish('CCCpqCorCsCCrpCtp', 'CD_CO')
    o4p = ci.parse_polish('CCCpqCorCsCCrpCsp', 'CD_CO')
    o5 = ci.parse_polish('CCpqCrCCCqsCopCtq', 'CD_CO')
    o5p = ci.parse_polish('CCpqCrCCCqsCopCrq', 'CD_CO')
    assert ci.canonical(substitute(o4, 'Vt', ('Vs', ()))) == ci.canonical(o4p)
    assert ci.canonical(substitute(o5, 'Vt', ('Vr', ()))) == ci.canonical(o5p)
    path = ci.ROOT / 'evidence/O5_AJL_legacy_O6_countermodel_verification.py'
    spec = importlib.util.spec_from_file_location('o5_matrix', path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    assert all(module.o6(p, q, r, s, r) in module.DESIGNATED
               for p, q, r, s in itertools.product(module.DOMAIN, repeat=4))
    assert module.lukasiewicz_l4(2, 1, 1, 3) not in module.DESIGNATED
    return {'proper_tautological_generalizations': 0, 'distinct_generalizations_checked': counts,
            'c1915_countervaluation_pqrst': [1, 0, 1, 0, 0],
            'O4_prime_is_t_to_s_instance': True, 'O5_prime_is_t_to_r_instance': True,
            'O5_prime_designated_valuations': 7**4, 'L4_countervalue': 7}


if __name__ == '__main__':
    result = verify()
    text = json.dumps(result, indent=2) + '\n'
    if '--write' in sys.argv:
        (ci.ROOT / 'reduction_checks.json').write_text(text)
    print(text, end='')
