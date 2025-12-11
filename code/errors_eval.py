import json
import ast
import sys
import traceback
from collections import defaultdict, Counter

# --- Configuration ---
# Point this to your results file
RESULTS_FILE = "/home/lucas/SOEN-TAES/SOEN-TAES/results/RQ1GPT5/MBPP-plus/RawGPT/results/flowgen_mbpp_plus_corrected_v2_eval_results.json" 
DATASET_TYPE = "mbpp"  # 'mbpp' or 'humaneval'

def analyze_error_type(code_snippet, entry_point, test_inputs):
    """
    Attempts to execute the code and run it against the failed inputs 
    to capture the specific exception type.
    """
    # 1. Check for Syntax Errors (Parsing)
    try:
        ast.parse(code_snippet)
    except SyntaxError:
        return "SyntaxError"
    except Exception:
        return "SyntaxError" # Other parse errors

    # 2. Define the execution environment
    local_scope = {}
    try:
        exec(code_snippet, globals(), local_scope)
    except Exception as e:
        # If it fails during definition (e.g., NameError in decorator, ImportError)
        return type(e).__name__

    # 3. Check if entry point exists
    if entry_point not in local_scope:
        return "EntryPointError (NameError)"
    
    func = local_scope[entry_point]

    # 4. Run against failed inputs to reproduce the runtime error
    # If no specific failed tests are listed but status is fail, it usually means 
    # it crashed before running tests or the test format wasn't captured.
    if not test_inputs:
        return "Unknown (Likely Logic/Assertion or Timeout)"

    for inputs in test_inputs:
        try:
            # Prepare arguments (handle single vs multiple args)
            if isinstance(inputs, list):
                func(*inputs)
            else:
                func(inputs)
        except AssertionError:
            return "AssertionError" # Logic error (Wrong Answer)
        except Exception as e:
            return type(e).__name__ # TypeError, ValueError, IndexError, etc.
            
    return "AssertionError" # Default if it runs but fails the check logic elsewhere

def main():
    print(f"--- Loading {RESULTS_FILE} ---")
    try:
        with open(RESULTS_FILE, 'r') as f:
            data = json.load(f)
    except FileNotFoundError:
        print(f"Error: File {RESULTS_FILE} not found.")
        return

    # Handle different JSON structures (EvalPlus sometimes outputs a dict or list)
    if "eval" in data:
        results = data["eval"] # Structure: {"Mbpp/1": [...]}
    else:
        results = data # List or direct dict

    error_counts = Counter()
    total_failures = 0
    
    print("--- Analyzing Failures ---")
    
    # Iterate through tasks
    # Determine iterator based on structure
    iterator = results.items() if isinstance(results, dict) else enumerate(results)
    
    for key, items in iterator:
        # EvalPlus results are often a list of generations per task. We take the first one (k=0).
        if isinstance(items, list):
            item = items[0]
        else:
            item = items

        task_id = item.get("task_id", key)
        status = item.get("base_status", "pass") # Check base status (or plus_status)
        
        if status == "fail":
            total_failures += 1
            
            # Extract details
            code = item.get("solution", "")
            fail_tests = item.get("base_fail_tests", [])
            
            # Extract Entry Point (Naive parsing or Dataset lookup required for perfect accuracy)
            # For MBPP/HumanEval, we can often guess or parse the last function defined.
            # Here we try to find the function name from the code string.
            entry_point = "unknown"
            try:
                tree = ast.parse(code)
                for node in tree.body:
                    if isinstance(node, ast.FunctionDef):
                        entry_point = node.name
                # If multiple, usually the last one is the entry point in these benchmarks
            except:
                pass

            # Analyze
            error_type = analyze_error_type(code, entry_point, fail_tests)
            error_counts[error_type] += 1
            
            # Optional: Print detailed logs for debugging
            # print(f"[{task_id}] -> {error_type}")

    print("\n" + "="*30)
    print(f"TOTAL FAILURES ANALYZED: {total_failures}")
    print("="*30)
    print(f"{'ERROR TYPE':<25} | {'COUNT':<5}")
    print("-" * 33)
    for error, count in error_counts.most_common():
        print(f"{error:<25} | {count:<5}")
    print("="*30)

if __name__ == "__main__":
    main()