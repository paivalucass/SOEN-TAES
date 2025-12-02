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
    test_prompt = '''
from typing import List

def has_close_elements(numbers: List[float], threshold: float) -> bool:
    """ Check if in given list of numbers, are any two numbers closer to each other than
    given threshold.
    >>> has_close_elements([1.0, 2.0, 3.0], 0.5)
    False
    >>> has_close_elements([1.0, 2.8, 3.0, 4.0, 5.0, 2.0], 0.3)
    True
    """
'''
    print(main(test_prompt, flowPath="rawGPT/rawGPT.json"))
    # print(main(test_prompt, flowPath="scrum/scrum.json"))
    # print(main(test_prompt, flowPath="testdriven/testdriven.json"))
    # print(main(test_prompt, flowPath="waterfall/waterfall.json"))
