#!/bin/env python3
# -*- coding: utf-8 -*-
# version: Python3.X
""" util
"""
import random
import os
import json
from openai import OpenAI 
from utils.keys.base_key import BaseKey
from utils.workflow import return_root_absolute_path

# Load keys
with open(os.path.join(return_root_absolute_path(), "conf.json"), "r") as f:
    api_key_list = json.load(f)["openai_key"]

class OpenaiAPI(BaseKey):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        # NEW: Initialize the client explicitly (v1.x style)
        # We pick a random key from your list
        self.client = OpenAI(api_key=random.choice(api_key_list))
        
        self.temperature = 1.0
        
        # --- MODEL SELECTION ---
        # self.model = "gpt-3.5-turbo-1106"  # OLD
        # self.model = "gpt-4o"                # NEW (Current State-of-the-Art)
        self.model = "gpt-5-nano"               # FUTURE (Uncomment if you have specific access)

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
        try_times = kwargs.get("try_times", 5)
        temperature = kwargs.get("temperature", self.temperature)
        for i in range(try_times):
            try:
                # NEW: v1.x Syntax
                completion = self.client.chat.completions.create(
                    model=self.model,
                    messages=[
                        {"role": "user", "content": prompt}
                    ],
                    temperature=temperature,
                    timeout=300,  
                )
                # We use .model_dump() to convert the object back to a dictionary
                # This ensures the rest of FlowGen (which expects a dict) doesn't break.
                return completion.choices[0].message.model_dump()
            except Exception as e:
                print(f"[-] ERROR calling openai: {e}")
                continue

    def json_response_prompt(self, prompt, **kwargs):
        try_times = kwargs.get("try_times", 5)
        temperature = kwargs.get("temperature", self.temperature)
        for i in range(try_times):
            try:
                # NEW: v1.x Syntax
                completion = self.client.chat.completions.create(
                    model=self.model,
                    messages=[
                        {"role": "user", "content": prompt}
                    ],
                    response_format={"type": "json_object"},
                    temperature=temperature,
                    timeout=300,
                )
                return completion.choices[0].message.model_dump()
            except Exception as e:
                print(f"[-] ERROR calling openai: {e}")
                continue

    def json_response_message(self, messages, **kwargs):
        try_times = kwargs.get("try_times", 5)
        temperature = kwargs.get("temperature", self.temperature)
        for i in range(try_times):
            try:
                # NEW: v1.x Syntax
                completion = self.client.chat.completions.create(
                    model=self.model,
                    messages=messages,
                    response_format={"type": "json_object"},
                    temperature=temperature,
                    timeout=300,
                )
                return completion.choices[0].message.model_dump()
            except Exception as e:
                print(f"[-] ERROR calling openai: {e}")
                continue

    def execute(self, version, **kwargs):
        return getattr(self, self.version_map[version])(**kwargs)


if __name__ == "__main__":
    pass