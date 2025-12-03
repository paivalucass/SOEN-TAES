#!/bin/env python3
# -*- coding: utf-8 -*-
# version: Python3.X
""" Entrance of this project
"""
import os
import json
from utils.workflow import Workflow, return_root_absolute_path

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

if __name__ == "__main__":
    # 1. Import HumanEval tools (ensure you installed human-eval)
    from human_eval.data import read_problems, write_jsonl
    import time
    
    # 2. Configuration
    # Select which workflow you want to test:
    FLOW_PATH = "rawGPT/rawGPT.json"         # Baseline
    # FLOW_PATH = "scrum/scrum.json"           # The Agent Framework
    # FLOW_PATH = "waterfall/waterfall.json"
    
    OUTPUT_FILE = "Chat_GPT5_flowgen_humaneval_results.jsonl"
    
    print(f"--- Starting Benchmark ---")
    print(f"Workflow: {FLOW_PATH}")
    print(f"Output File: {OUTPUT_FILE}")

    # 3. Load the dataset
    # This returns a dictionary: {"HumanEval/0": {...}, "HumanEval/1": {...}}
    problems = read_problems()
    
    samples = []
    
    # 4. Iterate through every problem in the benchmark
    for task_id, problem_data in problems.items():
        print(f"\nProcessing Task: {task_id}")
        
        # 'prompt' contains the function signature and docstring
        # e.g., "def has_close_elements(numbers, threshold): ..."
        prompt_text = problem_data['prompt']
        
        try:
            # 5. Call your existing main function
            # We pass the benchmark prompt into your workflow
            generated_code, workspace_path = main(prompt=prompt_text, flowPath=FLOW_PATH)
            
            # 6. Append to samples in the required format
            samples.append({
                "task_id": task_id,
                "completion": generated_code
            })
            print(f"Success! Workspace: {workspace_path}")

        except Exception as e:
            # Error handling is crucial so one crash doesn't stop the whole experiment
            print(f"ERROR on {task_id}: {e}")
            samples.append({
                "task_id": task_id,
                "completion": "" # Empty completion on failure
            })

    # 7. Save all results to a .jsonl file
    write_jsonl(OUTPUT_FILE, samples)
    print(f"\nBenchmark Complete. Results saved to {OUTPUT_FILE}")