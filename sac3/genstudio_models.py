import json
import os
import time
import openai
import persist_to_disk as ptd
from openai.error import APIError, RateLimitError
import genstudiopy
from genstudiopy import ChatCompletionGCP

# new call_genstudio with model and temperature as inputs - jiaxin, 07-20-2023
def call_genstudio(user_prompt, system_prompt, model, temperature):
    # avoid some stop due to errors 
    sleep = 1
    while True:
        try:
            # print(
            #     f"Calling genstudio from local with user_prompt={user_prompt}"
            # )
            result = genstudiopy.ChatCompletion.create(
                # model=default_config.genai_params.model_name_genstudio,
                model=model,
                messages=build_payload_message(user_prompt, system_prompt),
                temperature = temperature
            )
            out = result["choices"][0]["message"]["content"]
            break

        except Exception as e:
            print(e)
            for w in ['filtered', 'badWords', 'RiskService', 'Bad words', 'ValidationError']:
                if w in str(e):
                    return None
            sleep *= 2
            print('sleeping %i seconds...'%sleep)
            time.sleep(sleep)
    return out


def call_genstudio_palm(user_prompt, system_prompt, model, temperature, max_output_tokens):
    # avoid some stop due to errors 
    sleep = 1
    while True:
        try:
            result = genstudiopy.ChatCompletionGCP.create(
                model=model,
                context=system_prompt,
                examples=[],
                messages=[{'author': 'user', 'content': user_prompt}],
                max_output_tokens=max_output_tokens,
                temperature=temperature
            )
            out = result.predictions[0]['candidates'][0]['content']
            break

        except Exception as e:
            print(e)
            for w in ['filtered', 'badWords', 'RiskService', 'Bad words', 'ValidationError']:
                if w in str(e):
                    return None
            sleep *= 2
            print('sleeping %i seconds...'%sleep)
            time.sleep(sleep)
    return out

def build_payload_message(user_prompt, system_prompt=""):
    if system_prompt != "":
        return [
            {"role": "user", "content": user_prompt},
            {"role": "system", "content": system_prompt},
        ]
    else:
        return [
            {"role": "user", "content": user_prompt},
        ]



