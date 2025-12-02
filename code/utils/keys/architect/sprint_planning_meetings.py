#!/bin/env python3
# -*- coding: utf-8 -*-
# version: Python3.X
""" util
"""
import os
import json
import threading
from queue import Queue
from utils.keys.openai_api import OpenaiAPI
from utils.keys.base_key import BaseKey


class SprintPlanMeetings(BaseKey):
    version_map = {
        "0.0.2": "disordered",
    }

    def _disordered_meeting(self, workspace, history, role):
        openai_api = OpenaiAPI()
        for i in range(2):
            prompt = openai_api.generate_prompt_from_format_prompt("agile_disordered_meeting_discuss.json")

            prompt["Role"] += role
            prompt["Context"] = "\n".join(history.queue)

            prompt = json.dumps(prompt)
            result = openai_api.execute("default", prompt=prompt)["content"]
            history.put(f"[{role}]says: {result}\n-----\n")

    def disordered(self, workspace, **kwargs):
        openai_api = OpenaiAPI()
        q = Queue()
        q.put(f"[ScrumMaster]says: We have a job: {self._get_raw_question(workspace)}, do you have any ideas?\n-----\n")
        thread_list = list()
        roles = ["ProductOwner", "Architect", "Developer", "Tester"]

        for role in roles:
            thread_list.append(threading.Thread(target=self._disordered_meeting, args=(workspace, q, role)))
        for each_thread in thread_list:
            each_thread.start()
        for each_thread in thread_list:
            each_thread.join()

        self._write_log(workspace, "Discussion", "\n".join(q.queue))
        prompt = openai_api.generate_prompt_from_format_prompt("agile_disordered_meeting_conclusion.json")
        prompt["Context"] = "\n".join(q.queue)
        prompt = json.dumps(prompt)
        result = openai_api.execute("default_json_prompt", prompt=prompt)["content"]
        self._write_log(workspace, "DisorderedSprintMeetings", result, prompt=prompt)

        return result

    def execute(self, version, **kwargs):
        return getattr(self, self.version_map[version])(**kwargs)


if __name__ == "__main__":
    pass
