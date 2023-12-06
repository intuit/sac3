from sac3 import llm_models

def paraphrase(question, number, model, temperature):
    '''
    Inputs: 
    quesiton - original user query
    number - how many perturbed questions
    model - GPTs or open-sourced models
    temperature - typically we use 0 here 

    Output:
    perb_questions - perturbed questions that are semantically equivalent to the question
    '''

    perb_questions = []  
    prompt_temp = f'For question Q, provide {number} semantically equivalent questions.'
    prompt = prompt_temp + '\nQ:' + question

    res = llm_models.call_openai_model(prompt, model, temperature) # openai model call 
    res_split = res.split('\n')
    for i in range(len(res_split)):
        perb_questions.append(res_split[i])
    
    return perb_questions

