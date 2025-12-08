#!/bin/env python3
import os
import json
import argparse
import re
import threading 
from concurrent.futures import ThreadPoolExecutor, as_completed

# --- Libraries for benchmarks ---
from datasets import load_dataset 
from human_eval.data import read_problems

from utils.workflow import Workflow, return_root_absolute_path

workflow_dir = os.path.join(return_root_absolute_path(), "workflow")

# --- GLOBAL LOCK ---
file_lock = threading.Lock()

# --- HELPER: Extract Correct Function Name ---
def get_target_function_name(code_snippet):
    """
    Scans the reference code to find the function name.
    It returns the LAST defined function, which handles cases where
    helper functions are defined before the main entry point.
    """
    # Find all strings that look like "def function_name"
    matches = re.findall(r"def\s+([a-zA-Z_]\w*)(?=\s*\()", code_snippet)
    
    if matches:
        return matches[-1] # Return the last one (The main entry point)
    return None

# --- 1. The Core FlowGen Function ---
def main(prompt, flowPath):
    workflow = Workflow()
    flow = workflow.loads_workflow(file_path=os.path.join(workflow_dir, flowPath))
    workspace = workflow.create_workspace()
    
    for each_stage in flow:
        step_lists = each_stage["steps"]
        while len(step_lists) > 0:
            step = step_lists.pop(0)
            workflow.do_step(step, step['leader'], workspace=workspace, task=prompt, workflow=flowPath)
            
    with open(os.path.join(workspace, "log.json"), "r") as f:
        result = json.load(f)["FinalCode"]
    return result, workspace

# --- 2. The Worker Function (Updated) ---
def process_single_problem(item, dataset_type, flow_path):
    try:
        # --- A. PARSE INPUT ---
        if dataset_type == "humaneval":
            task_id = item[0]
            problem_data = item[1]
            raw_prompt = problem_data['prompt']
            target_name_instruction = "" # HumanEval usually includes the signature in the prompt
            
        elif dataset_type == "mbpp":
            # Ensure ID is formatted correctly for EvalPlus
            task_id = f"Mbpp/{item['task_id']}"
            
            # 1. Get the correct name from the reference code (The last def)
            target_name = get_target_function_name(item['code'])
            
            # 2. Add the specific name instruction to the prompt
            if target_name:
                raw_prompt = f"{item['prompt']}\n\nREQUIRED: You must name your function '{target_name}'."
            else:
                raw_prompt = item['prompt']

        # --- B. INJECT STRICT INSTRUCTIONS ---
        strict_wrapper = (
            f"{raw_prompt}\n\n"
            "IMPORTANT INSTRUCTION:\n"
            "1. You are a code generator. Write the solution in Python.\n"
            "2. Output ONLY the valid Python code. Do not write 'Here is the code'.\n"
            "3. Do not wrap the code in markdown blocks (no ```).\n"
            "4. Do not include usage examples or tests outside the function."
        )

        # --- C. RUN FLOWGEN ---
        generated_code, _ = main(prompt=strict_wrapper, flowPath=flow_path)

        return {"task_id": task_id, "completion": generated_code}

    except Exception as e:
        # Fallback ID extraction for error logging
        t_id = item[0] if dataset_type == "humaneval" else f"Mbpp/{item.get('task_id', '?')}"
        print(f"FAILED Task {t_id}: {e}")
        return {"task_id": t_id, "completion": ""}
    
# --- 3. Immediate Save Function ---
def save_result_immediately(filepath, result_dict):
    json_str = json.dumps(result_dict)
    with file_lock:
        with open(filepath, 'a') as f: 
            f.write(json_str + "\n")

# --- 4. Main Execution Block ---
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Run FlowGen on Benchmarks')
    parser.add_argument('--dataset', type=str, required=True, choices=['humaneval', 'mbpp'], 
                        help='Which benchmark to run')
    parser.add_argument('--workers', type=int, default=5, 
                        help='Number of parallel threads (default: 5)')
    args = parser.parse_args()

    # Configuration
    # FLOW_PATH = "rawGPT/rawGPT.json"         # Baseline
    FLOW_PATH = "scrum/scrum.json"
    # FLOW_PATH = "waterfall/waterfall.json"      
    
    if args.dataset == "humaneval":
        print("--- Loading HumanEval ---")
        raw_data = read_problems()
        tasks_list = list(raw_data.items()) 
        output_file = "flowgen_humaneval_results.jsonl"
        
    elif args.dataset == "mbpp":
        print("--- Loading MBPP-Plus (EvalPlus Standard) ---")
        dataset = load_dataset("evalplus/mbppplus", split="test")
        tasks_list = [item for item in dataset]
        output_file = "flowgen_mbpp_plus_results.jsonl"
        
    print(f"Workflow: {FLOW_PATH}")
    print(f"Output File: {output_file}")
    print(f"Total Tasks: {len(tasks_list)}")
    print(f"Workers: {args.workers}")

    print("Initializing output file...")
    with open(output_file, 'w') as f:
        pass 

    with ThreadPoolExecutor(max_workers=args.workers) as executor:
        future_to_task = {
            executor.submit(process_single_problem, item, args.dataset, FLOW_PATH): item 
            for item in tasks_list
        }

        for future in as_completed(future_to_task):
            try:
                result = future.result()
                save_result_immediately(output_file, result)
                print(f"Finished & Saved: {result['task_id']}")
            except Exception as exc:
                print(f"Thread exception: {exc}")

    print(f"Done. All results saved to {output_file}")