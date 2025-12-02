#!/bin/env python3
# -*- coding: utf-8 -*-
# version: Python3.X
""" util
"""
import os
import json
from utils.keys.openai_api import OpenaiAPI
from utils.keys.base_key import BaseKey


class RawChatGPT(BaseKey):
    version_map = {
        "0.0.2": "version_0_0_2"
    }

    def version_0_0_2(self, workspace, **kwargs):
        openai = OpenaiAPI()
        question = self._get_raw_question(workspace)
        result = openai.execute("default", prompt=json.dumps(question))["content"]
        self._write_log(workspace, 'Prompt', json.dumps(question))
        self._write_log(workspace, 'FinalCode', result)
        return result

    def execute(self, version, **kwargs):
        return getattr(self, self.version_map[version])(**kwargs)


if __name__ == "__main__":
    pass
