from Globals import *
from ModelTools import *
from TreeForms import *
from TheoremProverUtils import *

parser = argparse.ArgumentParser(description="General process runner. Able to handle standard computation, hammering out remaining with vampire, and filtering out with Prover9.")

parser.add_argument("name", type=str, help="Run name")
parser.add_argument("target_length", type=int, help="Targeted Length")
parser.add_argument("config_file", type=str, help="File for run configuration")
#parser.add_argument("--progress_tracker_override", type=int, help="Progress tracker override", default=-1)
parser.add_argument("--run_type", type=str, help="Run type, 'Standard' (default), 'Hammer', or 'Prover9Hammer'", default="Standard")
parser.add_argument("--cache_size", type=int, help="Cache Size. TODO'", default=14)
parser.add_argument("--reset_progress", action='store_true', help="Should current progress be reset (start from the first form)")
parser.add_argument("--full_verification", action='store_true', help="Should full verification be ran. WARNING: VERY VERY VERY VERY VERY SLOW")
parser.add_argument("--retain_input_files", action='store_true', help="Should input files be retained after a prover9 or vampire run is completed (for debugging)")
parser.add_argument("--vampire_time_limit", type=int, default=10, help="Per-candidate Vampire time limit in seconds")
parser.add_argument("--vampire_memory_limit", type=int, default=4096, help="Per-candidate Vampire memory limit in MiB")
parser.add_argument("--vampire_cores", type=int, default=1, help="Vampire cores per candidate")
parser.add_argument("--stats_file", type=str, default=None, help="JSON statistics output (defaults under partial_run_saves)")
parser.add_argument("--model_namespace", type=str, default=None, help="CounterModels subdirectory to load and extend (defaults to run name)")
parser.add_argument("--shard_index", type=int, default=0, help="Zero-based structural-form shard index")
parser.add_argument("--shard_count", type=int, default=1, help="Number of disjoint structural-form shards")

args = parser.parse_args()

if args.shard_count < 1 or not 0 <= args.shard_index < args.shard_count:
    parser.error("require shard_count >= 1 and 0 <= shard_index < shard_count")

name: str = args.name
target_length: int = args.target_length
with open(args.config_file, "r") as f:
    config = json.load(f)
    config_name: str = config.get("name")
    predicate: PredicateSpec = PredicateSpec.parse(config.get("predicate"))
    operators: tuple[OperationSpec, ...] = tuple([OperationSpec.parse(op) for op in config.get("operators")])
    constants: tuple[ConstantSpec, ...] = tuple([ConstantSpec.parse(cons) for cons in config.get("constants")])

    spec: ModelSpec = ModelSpec(predicate, operators, constants)

    vampire_template: str = "\n".join(config.get("vampire_template"))+"\n"
    prover9_template: str = "\n".join(config.get("prover9_template"))+"\n"

    known_tautologies: list[str] | None = config.get("known_tautologies")

run_type: str = args.run_type
cache_size: int = args.cache_size
#print(name)
#print(target_length)
#print(spec)
#print(vampire_template)
#print(run_type)
#print(cache_size)

vampire_executable_file_path = os.path.join("theorem_provers", "vampire")
prover9_executable_file_path = os.path.join("theorem_provers", "prover9")
unsolved_folder = os.path.join("Remaining",name)
unsolved_file = os.path.join(unsolved_folder, name+str(target_length)+"Rem.txt")
counter_model_folder = os.path.join("CounterModels", args.model_namespace or name)
save_file_base = os.path.join("partial_run_saves", name)
reset_progress = args.reset_progress
full_verification = args.full_verification
remove_temp_files = not args.retain_input_files

tree_form = TreeForm(spec, cache_size)

#print("===============")
#print(dict(tree_form._formula_count_helper(1)))
#print(3 + 1 - tree_form.predicate.arity)
#print(list(tree_form._node_size_combos(tree_form.predicate.arity, 3 + 1 - tree_form.predicate.arity, tree_form.predicate.associative)))
#print(list(tree_form.valid_node_size_combos(tree_form.predicate.arity, 3 + 1 - tree_form.predicate.arity, tree_form.predicate.associative)))
#for i in range(1, 7+1):
#    print(f"{i}:{dict(tree_form._formula_count_helper(i))}")
#for i in range(1, 7+1):
#    print(f"{i}:{tree_form._formula_count_predicate_extension(i)}")
#print(tree_form.formula_count(7))
#default_degeneracy = np.ones(3, dtype=np.int8)
#print(list(k.tptp() for k in tree_form.new_node(3).get_iterator(default_degeneracy)))

#tree_form.verify_formulas(7)


Models = ModelTable(spec, counter_model_folder=counter_model_folder)
if known_tautologies:
    Models.verify_known_formulas(known_tautologies)

if not os.path.exists(unsolved_folder):
    os.makedirs(unsolved_folder)

match run_type:
    case "Standard":
        vampire_wrapper: TheoremProverWrapper = VampireWrapper(
            vampire_executable_file_path,
            vampire_template,
            counter_model_folder,
            Models.spec,
            verify_models=True,
            optional_args={
                "--time_limit": str(args.vampire_time_limit),
                "--memory_limit": str(args.vampire_memory_limit),
                "--cores": str(args.vampire_cores),
            },
            remove_temp_files=remove_temp_files,
        )

        print("Starting length: "+str(target_length))
        start_time = time.time()
        progress_tracker = ProgressTracker(tree_form.form_count(target_length))
        save_file = save_file_base+str(target_length)+".txt"
        stats_file = args.stats_file or save_file_base+str(target_length)+".stats.json"
        if os.path.exists(stats_file) and not reset_progress:
            statistics = ProcessStatistics.read_json(stats_file)
            if not statistics.counters_reconcile:
                raise RuntimeError(
                    "Refusing to resume from non-reconciling statistics: "
                    + stats_file
                    + ". Preserve this diagnostic artifact and use a fresh run name."
                )
        else:
            statistics = ProcessStatistics()
        statistics.run_name = name
        statistics.target_length = target_length
        statistics.config_file = args.config_file
        statistics.length_convention = (
            "connective, constant, and variable occurrences"
            if predicate.symbol != "="
            else "all symbols in both terms plus one equality symbol"
        )
        statistics.vampire_command = vampire_wrapper.command + ["--input_syntax", "tptp", "<candidate.in>"]
        global_structural_forms = tree_form.form_count(target_length)
        global_candidate_instances = tree_form.formula_count(target_length)
        statistics.shard_index = args.shard_index
        statistics.shard_count = args.shard_count
        statistics.global_expected_structural_forms = global_structural_forms
        statistics.global_expected_candidate_instances = global_candidate_instances
        statistics.expected_structural_forms = shard_item_count(
            global_structural_forms, args.shard_index, args.shard_count
        )
        statistics.expected_candidate_instances = (
            global_candidate_instances if args.shard_count == 1 else 0
        )
        statistics.countermodels_loaded_at_start = len(Models.counter_models)
        statistics.started_at = datetime.now().astimezone().isoformat()
        survivor_details_file = os.path.join(unsolved_folder, name+str(target_length)+"Survivors.jsonl")
        unsolved_count, processed_count = tree_form.process_tree(
            target_length, Models, vampire_wrapper, unsolved_file,
            progress_tracker, save_file, reset_progress, full_verification,
            statistics, stats_file, survivor_details_file,
            args.shard_index, args.shard_count,
        )
        statistics.finished_at = datetime.now().astimezone().isoformat()
        statistics.elapsed_seconds += time.time() - start_time
        statistics.countermodels_at_end = len(Models.counter_models)
        statistics.write_json(stats_file)

        print("Processed "+str(processed_count)+" formulas, Was unable to solve: "+str(unsolved_count))
        print("Statistics: "+stats_file)
        print(json.dumps(statistics.to_dict(), indent=2))
    
        print("Execution time: "+str(time.time() - start_time))
    case "Hammer":
        vampire_wrapper: TheoremProverWrapper = VampireWrapper(vampire_executable_file_path, vampire_template, counter_model_folder, Models.spec, verify_models=True, optional_args={"--time_limit": "2"}, remove_temp_files=remove_temp_files)
        
        print("Starting length: "+str(target_length))
        vampire_wrapper.hammer(unsolved_file)
    case "Prover9Hammer":
        prover9_wrapper: TheoremProverWrapper = Prover9Wrapper(prover9_executable_file_path, Models.spec, prover9_template, remove_temp_files=remove_temp_files)

        print("Starting length: "+str(target_length))
        new_unsolved_file = os.path.join(unsolved_folder, name+str(target_length)+"Rem-fastpass.txt")
        prover9_wrapper.hammer(unsolved_file, new_unsolved_file)
