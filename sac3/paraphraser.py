from sac3 import llm_models

def paraphrase(question, number, model, temperature):
    perb_question = []  
    prompt_temp = f'For question Q, provide {number} semantically equivalent questions.'
    prompt = prompt_temp + '\nQ:' + question

    res = llm_models.call_openai_model(prompt, model, temperature) # openai model call 
    res_split = res.split('\n')
    for i in range(len(res_split)):
        perb_question.append(res_split[i])
    
    return perb_question

