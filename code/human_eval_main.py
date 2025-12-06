#!/bin/env python3
# -*- coding: utf-8 -*-
# version: Python3.X
""" Entrance of this project
"""
import os
import json
from utils.workflow import Workflow, return_root_absolute_path
from concurrent.futures import ThreadPoolExecutor, as_completed



workflow_dir = os.path.join(return_root_absolute_path(), "workflow")


def main(prompt, flowPath=f"rawGPT/rawGPT.json"):
    # loads workflow
    workflow = Workflow()
    flow = workflow.loads_workflow(file_path=os.path.join(workflow_dir, flowPath))
    # run workflow
    workspace = workflow.create_workspace()
    for each_stage in flow:
        step_lists = each_stage["steps"]
        print(f"[*] Stage:{each_stage['stage']}")
        while len(step_lists) > 0:
            step = step_lists.pop(0)
            print(f"[*] Step:{step['key']}, Leader:{step['leader']}, Version:{step['key version']}")
            workflow.do_step(step, step['leader'], workspace=workspace, task=prompt, workflow=flowPath)
    with open(os.path.join(workspace, "log.json"), "r") as f:
        result = json.load(f)["FinalCode"]
    return result, workspace

def process_single_problem(item):
    """Helper function to run one benchmark task"""
    task_id, problem_data = item
    prompt_text = problem_data['prompt']
    
    
    task_number = int(task_id.split("/")[-1])
    
    if (task_number < 27):
        return {"task_id": task_id, "completion": ""}
    
    try:
        # Run FlowGen
        generated_code, _ = main(prompt=prompt_text, flowPath=FLOW_PATH)
        # Clean the code (remove markdown)
        return {"task_id": task_id, "completion": generated_code}
    except Exception as e:
        print(f"FAILED {task_id}: {e}")
        return {"task_id": task_id, "completion": ""}

if __name__ == "__main__":
    # 1. Import HumanEval tools (ensure you installed human-eval)
    from human_eval.data import read_problems, write_jsonl
    import time

    # 2. Configuration
    # Select which workflow you want to test:
    # FLOW_PATH = "rawGPT/rawGPT.json"         # Baseline
    FLOW_PATH = "scrum/scrum.json"
    # FLOW_PATH = "waterfall/waterfall.json"

    OUTPUT_FILE = "Chat_GPT5_flowgen_humaneval_results.jsonl"

    print(f"--- Starting Benchmark ---")
    print(f"Workflow: {FLOW_PATH}")
    print(f"Output File: {OUTPUT_FILE}")

    problems = read_problems()
    
    samples = []
    
    # RUN PARALLEL (5 workers means 5 problems running at once)
    # Don't go too high or you will hit OpenAI Rate Limits!
    MAX_WORKERS = 5
    
    print(f"Starting Parallel Execution with {MAX_WORKERS} workers...")
    
    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
        # Submit all tasks
        future_to_task = {executor.submit(process_single_problem, item): item[0] for item in problems.items()}
        
        for future in as_completed(future_to_task):
            task_id = future_to_task[future]
            try:
                result = future.result()
                samples.append(result)
                print(f"Completed: {task_id}")
            except Exception as exc:
                print(f"{task_id} generated an exception: {exc}")

    write_jsonl(OUTPUT_FILE, samples)
    print("Done.")