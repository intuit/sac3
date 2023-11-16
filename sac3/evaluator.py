from sac3 import llm_models

class Evaluate:
    def __init__(self, model):
        self.model = model
        self.prompt_temp = 'Answer the following question:\n'
    
    def self_evaluate(self, self_question, temperature, self_num):
        self_response = []  
        prompt = self.prompt_temp + '\nQ:' + self_question
    
        for i in range(self_num): 
            # llm model: openai, genstudio, open-source models (falcon, guanaco)
            if self.model in ['gpt-3.5-turbo','gpt-4']:
                res = llm_models.call_openai_model(prompt, self.model, temperature) # openai model call
            elif self.model == 'guanaco-33b':
                res = llm_models.call_guanaco_33b(prompt, max_new_tokens = 200)
            elif self.model == 'falcon-7b':
                res = llm_models.call_falcon_7b(prompt, max_new_tokens = 200)
            # other open-sourced llms 
            self_response.append(res)

        return self_response
    
    def perb_evaluate(self, perb_question, temperature):
        perb_response = []  
        for i in range(len(perb_question)):
            prompt = self.prompt_temp + '\nQ:' + perb_question[i]
            # llm model: openai, genstudio, open-source models (falcon, guanaco)
            if self.model in ['gpt-3.5-turbo','gpt-4']:
                res = llm_models.call_openai_model(prompt, self.model, temperature) # openai model call 
            elif self.model == 'guanaco-33b':
                res = llm_models.call_guanaco_33b(prompt, max_new_tokens = 200)
            elif self.model == 'falcon-7b':
                res = llm_models.call_falcon_7b(prompt, max_new_tokens = 200)
            # other open-sourced llms 
            perb_response.append(res)
  
        return perb_response
