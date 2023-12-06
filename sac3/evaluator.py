from sac3 import llm_models

class Evaluate:
    def __init__(self, model):
        self.model = model
        self.prompt_temp = 'Answer the following question:\n'
    
    def self_evaluate(self, self_question, temperature, self_num):
        '''
        Inputs: 
        self_question - original user query 
        temperature - [0,1] for LLM randomness
        self_num - how many generated responses given this question

        Outputs:
        self_responses - generated responses given this question with different temperatures
        '''

        self_responses = []  
        prompt = self.prompt_temp + '\nQ:' + self_question
    
        for i in range(self_num): 
            # llm model: GPTs, open-source models (falcon, guanaco)
            if self.model in ['gpt-3.5-turbo','gpt-4']:
                res = llm_models.call_openai_model(prompt, self.model, temperature) # openai model call
            elif self.model == 'guanaco-33b':
                res = llm_models.call_guanaco_33b(prompt, max_new_tokens = 200)
            elif self.model == 'falcon-7b':
                res = llm_models.call_falcon_7b(prompt, max_new_tokens = 200)
            # other open-sourced llms 
            self_responses.append(res)

        return self_responses
    
    def perb_evaluate(self, perb_questions, temperature):
        '''
        Inputs: 
        perb_questions - perturbed questions that are semantically equivalent to the original question
        temperature - [0,1] for LLM randomness

        Outputs:
        perb_responses - generated responses given the perturbed questions
        '''
        
        perb_responses = []  
        for i in range(len(perb_questions)):
            prompt = self.prompt_temp + '\nQ:' + perb_questions[i]
            # llm model: GPTs, open-source models (falcon, guanaco)
            if self.model in ['gpt-3.5-turbo','gpt-4']:
                res = llm_models.call_openai_model(prompt, self.model, temperature) # openai model call 
            elif self.model == 'guanaco-33b':
                res = llm_models.call_guanaco_33b(prompt, max_new_tokens = 200)
            elif self.model == 'falcon-7b':
                res = llm_models.call_falcon_7b(prompt, max_new_tokens = 200)
            # other open-sourced llms 
            perb_responses.append(res)
  
        return perb_responses
