#!/bin/env python3
import os
import json
from concurrent.futures import ThreadPoolExecutor, as_completed
# NEW: Import datasets to load MBPP
from datasets import load_dataset 
from utils.workflow import Workflow, return_root_absolute_path

workflow_dir = os.path.join(return_root_absolute_path(), "workflow")

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

def process_single_mbpp_task(item):
    """Helper function for MBPP"""
    task_id = item['task_id']
    prompt_text = item['text']  

    try:
        # Run FlowGen
        generated_code, _ = main(prompt=prompt_text, flowPath=FLOW_PATH)
        
        # Return in the format EvalPlus/BigCode expects
        return {"task_id": task_id, "completion": generated_code}
    except Exception as e:
        print(f"FAILED {task_id}: {e}")
        return {"task_id": task_id, "completion": ""}

if __name__ == "__main__":
    # Configuration
    FLOW_PATH = "scrum/scrum.json"
    OUTPUT_FILE = "Chat_GPT5_flowgen_mbpp_results.jsonl"
    MAX_WORKERS = 5

    print(f"--- Starting MBPP Benchmark ---")
    
    # 1. LOAD MBPP (Sanitized)
    # The paper uses the sanitized version 
    dataset = load_dataset("mbpp", "sanitized", split="test")
    
    samples = []
    
    print(f"Starting Parallel Execution with {MAX_WORKERS} workers...")
    
    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        future_to_task = {executor.submit(process_single_mbpp_task, item): item['task_id'] for item in dataset}
        
        for future in as_completed(future_to_task):
            task_id = future_to_task[future]
            try:
                result = future.result()
                samples.append(result)
                print(f"Completed Task: {task_id}")
            except Exception as exc:
                print(f"Task {task_id} generated an exception: {exc}")

    # 2. SAVE JSONL
    with open(OUTPUT_FILE, 'w') as f:
        for sample in samples:
            f.write(json.dumps(sample) + "\n")
            
    print(f"Done. Results saved to {OUTPUT_FILE}")