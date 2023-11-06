from sac3 import llm_models
from sac3 import genstudio_models

def paraphrase(question, number, model, temperature):
    perb_question = []  
    prompt_temp = f'For question Q, provide {number} semantically equivalent questions.'
    prompt = prompt_temp + '\nQ:' + question

    res = genstudio_models.call_genstudio(prompt, '', model, temperature) # genstudio - pass
    # res = llm_models.call_openai_model(prompt, model, temperature) # openai - pass

    res_split = res.split('\n')
    for i in range(len(res_split)):
        perb_question.append(res_split[i])
    
    return perb_question

