#!/bin/env python3
import os
import json
import argparse
import re
import threading  # <--- NEW: Required for safe writing
from concurrent.futures import ThreadPoolExecutor, as_completed

# --- Libraries for benchmarks ---
from datasets import load_dataset 
from human_eval.data import read_problems

from utils.workflow import Workflow, return_root_absolute_path

workflow_dir = os.path.join(return_root_absolute_path(), "workflow")

# --- GLOBAL LOCK ---
# This prevents 2 threads from writing to the file at the exact same time
file_lock = threading.Lock()

# --- 1. The Core FlowGen Function (Unchanged) ---
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

# --- 2. The Worker Function ---
def process_single_problem(item, dataset_type, flow_path):
    try:
        # --- A. PARSE INPUT ---
        if dataset_type == "humaneval":
            task_id = item[0]
            problem_data = item[1]
            prompt_text = problem_data['prompt']
            
        elif dataset_type == "mbpp":
            task_id = item['task_id']
            prompt_text = item['text']

        # --- B. RUN FLOWGEN ---
        generated_code, _ = main(prompt=prompt_text, flowPath=flow_path)
                
        return {"task_id": task_id, "completion": generated_code}

    except Exception as e:
        t_id = item[0] if dataset_type == "humaneval" else item['task_id']
        print(f"FAILED Task {t_id}: {e}")
        return {"task_id": t_id, "completion": ""}

# --- 3. NEW: Immediate Save Function ---
def save_result_immediately(filepath, result_dict):
    """
    Appends a single result to the file safely using a lock.
    """
    json_str = json.dumps(result_dict)
    
    # Acquire the lock before opening the file
    with file_lock:
        with open(filepath, 'a') as f: # 'a' for Append mode
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
    FLOW_PATH = "scrum/scrum.json"  
    
    # Setup based on argument
    if args.dataset == "humaneval":
        print("--- Loading HumanEval ---")
        raw_data = read_problems()
        tasks_list = list(raw_data.items()) 
        output_file = "flowgen_humaneval_results.jsonl"
        
    elif args.dataset == "mbpp":
        print("--- Loading MBPP (Sanitized) ---")
        dataset = load_dataset("mbpp", "sanitized", split="test")
        tasks_list = [item for item in dataset]
        output_file = "flowgen_mbpp_results.jsonl"

    print(f"Workflow: {FLOW_PATH}")
    print(f"Output File: {output_file}")
    print(f"Total Tasks: {len(tasks_list)}")
    print(f"Workers: {args.workers}")

    # --- CRITICAL STEP: Initialize File ---
    # We open in 'w' mode once to clear old data or create the file
    print("Initializing output file...")
    with open(output_file, 'w') as f:
        pass # Just creating/clearing the file

    # Run Parallel Execution
    with ThreadPoolExecutor(max_workers=args.workers) as executor:
        future_to_task = {
            executor.submit(process_single_problem, item, args.dataset, FLOW_PATH): item 
            for item in tasks_list
        }

        for future in as_completed(future_to_task):
            try:
                result = future.result()
                
                # --- SAVE IMMEDIATELY HERE ---
                save_result_immediately(output_file, result)
                
                print(f"Finished & Saved: {result['task_id']}")
            except Exception as exc:
                print(f"Thread exception: {exc}")

    print(f"Done. All results saved to {output_file}")