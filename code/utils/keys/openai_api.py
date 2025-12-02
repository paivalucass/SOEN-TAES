#!/bin/env python3
# -*- coding: utf-8 -*-
# version: Python3.X
""" util
"""
import random
import openai
import os
import json
from utils.keys.base_key import BaseKey
from utils.workflow import return_root_absolute_path


with open(os.path.join(return_root_absolute_path(), "conf.json"), "r") as f:
    api_key = json.load(f)["openai_key"]


class OpenaiAPI(BaseKey):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        openai.api_key = random.choice(api_key)
        self.temperature = 0.8
        # self.model = "gpt-3.5-turbo-0613"
        # self.model = "gpt-3.5-turbo-0301"
        self.model = "gpt-3.5-turbo-1106"
        # self.model = "gpt-3.5-turbo-0125"

    version_map = {
        "default": "version_0_0_1",
        "default_json_prompt": "json_response_prompt",
        "default_json_message": "json_response_message",
        "0.0.1": "version_0_0_1"
    }

    def generate_prompt_from_unify_prompt(self, template_name):
        with open(os.path.join(self.format_prompt_templates, "basic_prompt.json"), "r", encoding="utf8") as f:
            prompt = json.load(f)
        with open(os.path.join(self.unify_prompt_templates, template_name), "r", encoding="utf8") as f:
            template = json.load(f)
        for key, value in template.items():
            if str(value) != "":
                prompt[key] = value
        return prompt

    def generate_prompt_from_format_prompt(self, template_name):
        with open(os.path.join(self.format_prompt_templates, "basic_prompt.json"), "r", encoding="utf8") as f:
            prompt = json.load(f)
        with open(os.path.join(self.format_prompt_templates, template_name), "r", encoding="utf8") as f:
            template = json.load(f)
        for key, value in template.items():
            if str(value) != "":
                prompt[key] = value
        return prompt

    def version_0_0_1(self, prompt, **kwargs):
        try_times = kwargs.get("try_times", 3)
        temperature = kwargs.get("temperature", self.temperature)
        for i in range(try_times):
            try:
                completion = openai.ChatCompletion.create(
                    model=self.model,
                    messages=[
                        {"role": "user", "content": prompt}
                    ],
                    temperature=temperature,
                    request_timeout=1 * 60,
                )
                return completion.choices[0].message
            except Exception as e:
                print(f"[-] ERROR calling openai: {e}")
                continue

    def json_response_prompt(self, prompt, **kwargs):
        model = self.model
        if model == "gpt-3.5-turbo-0613" or model == "gpt-3.5-turbo-0301":
            return self.version_0_0_1(prompt, **kwargs)
        try_times = kwargs.get("try_times", 3)
        temperature = kwargs.get("temperature", self.temperature)
        for i in range(try_times):
            try:
                completion = openai.ChatCompletion.create(
                    model=model,
                    messages=[
                        {"role": "user", "content": prompt}
                    ],
                    response_format={"type": "json_object"},
                    temperature=temperature,
                    request_timeout=1 * 60,
                )
                return completion.choices[0].message
            except Exception as e:
                print(f"[-] ERROR calling openai: {e}")
                continue

    def json_response_message(self, messages, **kwargs):
        try_times = kwargs.get("try_times", 3)
        temperature = kwargs.get("temperature", self.temperature)
        for i in range(try_times):
            try:
                completion = openai.ChatCompletion.create(
                    model=self.model,
                    messages=messages,
                    response_format={"type": "json_object"},
                    temperature=temperature,
                    request_timeout=1 * 60,
                )
                return completion.choices[0].message
            except Exception as e:
                print(f"[-] ERROR calling openai: {e}")
                continue

    def execute(self, version, **kwargs):
        return getattr(self, self.version_map[version])(**kwargs)


if __name__ == "__main__":
    pass