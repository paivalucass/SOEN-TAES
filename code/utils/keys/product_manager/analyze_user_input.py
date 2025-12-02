#!/bin/env python3
# -*- coding: utf-8 -*-
# version: Python3.X
""" util
"""
import json
import os
from utils.keys.base_key import BaseKey
from utils.keys.openai_api import OpenaiAPI


class AnalyzeUserInput(BaseKey):
    version_map = {
        "0.0.2": "waterfall",
        "0.0.4": "tdd_analyze_with_meetings"
    }

    def _prompt_for_waterfall(self, workspace, openai_api):
        prompt = openai_api.generate_prompt_from_unify_prompt("unify_write_analyze.json")
        prompt["Role"] += "Product Requirement Document"
        prompt["Question"] += self._get_raw_question(workspace)
        return json.dumps(prompt)

    def waterfall(self, workspace, **kwargs):
        openai_api = OpenaiAPI()
        prompt = self._prompt_for_waterfall(workspace, openai_api)
        result = openai_api.execute("default_json_prompt", prompt=prompt)["content"]
        self._write_log(workspace, 'Original PRD', result, prompt=prompt)
        return result

    def tdd_analyze_with_meetings(self, workspace, **kwargs):
        openai_api = OpenaiAPI()

        # Draft version
        prompt = openai_api.generate_prompt_from_unify_prompt("unify_write_analyze.json")
        prompt["Role"] += "requirement analyst"
        prompt["Question"] += self._get_raw_question(workspace)
        draft = openai_api.execute("default_json_prompt", prompt=json.dumps(prompt))["content"]
        self._write_log(workspace, 'AnalyzeDraft', draft)

        # meetings
        prompt = openai_api.generate_prompt_from_unify_prompt("unify_analyze_meetings.json")
        prompt["Context"] = draft
        review = openai_api.execute("default_json_prompt", prompt=json.dumps(prompt))["content"]
        self._write_log(workspace, 'AnalyzeMeetings', review)

        # revise version
        prompt = openai_api.generate_prompt_from_unify_prompt("unify_revise_analyze.json")
        prompt["Context"] = f"# Suggestion:\n{review}"
        prompt["Question"] += draft
        result = openai_api.execute("default_json_prompt", prompt=json.dumps(prompt))["content"]
        self._write_log(workspace, 'Analyze', result)

        return result

    def execute(self, version, **kwargs):
        return getattr(self, self.version_map[version])(**kwargs)


if __name__ == "__main__":
    pass
