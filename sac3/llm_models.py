import os
os.environ['HUGGINGFACE_HUB_CACHE'] = '/home/ec2-user/SageMaker/hf_cache'
os.environ['HF_HOME'] = '/home/ec2-user/SageMaker/hf_cache'

import openai
import torch
from peft import PeftModel
import transformers
from transformers import AutoModelForCausalLM, AutoTokenizer
import time

# Initialize OpenAI API
# openai.api_key = 'your openai key'

def call_openai_model(prompt, model, temperature):
    response = None
    while response is None:
        try:
            response = openai.ChatCompletion.create(
                model=model,
                messages=[
                    {"role": "system", "content": "You are a helpful assistant."},
                    {"role": "user", "content": prompt},
                ],
                temperature = temperature
                )

        except Exception as e:
            if 'is greater than the maximum' in str(e):
                raise BatchSizeException()
            print(e)
            print('Retrying...')
            time.sleep(2)
        try:
            output = response.choices[0].message.content
        except Exception:
            output = 'do not have reponse from chatgpt'
    return output 


def call_guanaco_33b(prompt, max_new_tokens):
    # 16 float 
    model_name = "huggyllama/llama-30b"
    adapters_name = 'timdettmers/guanaco-33b'
    model = AutoModelForCausalLM.from_pretrained(
        model_name,
        torch_dtype=torch.bfloat16,
        device_map="auto",
        # offload_folder="/home/ec2-user/SageMaker/hf_cache",
        max_memory= {i: '16384MB' for i in range(torch.cuda.device_count())}, # V100 16GB
    )
    model = PeftModel.from_pretrained(model, adapters_name)
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    
    # prompt 
    formatted_prompt = (
        f"A chat between a curious human and an artificial intelligence assistant."
        f"The assistant gives helpful, concise, and polite answers to the user's questions.\n"
        f"### Human: {prompt} ### Assistant:"
    )
    inputs = tokenizer(formatted_prompt, return_tensors="pt").to("cuda:0")
    outputs = model.generate(inputs=inputs.input_ids, max_new_tokens=max_new_tokens)
    res = tokenizer.decode(outputs[0], skip_special_tokens=True)
    res_sp = res.split('###')
    output = res_sp[1] + res_sp[2]
    
    return output 
    
    
def call_falcon_7b(prompt, max_new_tokens):
    # 16 float     
    model = "tiiuae/falcon-7b-instruct"
    tokenizer = AutoTokenizer.from_pretrained(model)
    pipeline = transformers.pipeline(
        "text-generation",
        model=model,
        tokenizer=tokenizer,
        torch_dtype=torch.bfloat16,
        trust_remote_code=True,
        device_map="auto"
    )
    sequences = pipeline(
        prompt,
        max_new_tokens=max_new_tokens,
        do_sample=True,
        top_k=10,
        num_return_sequences=1,
        eos_token_id=tokenizer.eos_token_id,
    )
    for seq in sequences:
        res = seq['generated_text']

    return res
