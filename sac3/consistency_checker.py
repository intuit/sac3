from sac3 import llm_models

class SemanticConsistnecyCheck:
    def __init__(self, model):
        self.model = model
        self.prompt_temp = """
        Are the following two Question-Answer(QA) pairs semantically equivalent? 
        Provide your best guess and the probability that it is correct (0.0 to 1.0).
        Given ONLY the guess (Yes or No) and probability, no other words or explanation. 
        For example:
        Guess: <most likely guess, as short as possible; not a complete sentence, just the guess!> 
        Probability: <the probability between 0.0 and 1.0 that your guess is correct, without any extra commentary whatsoever; 
        just the probability!>
        """
        
    def score_scc(self, question, target_answer, candidate_answers, temperature):
        '''
        Inputs:
        question - original user query
        target_answer - generated response given the original question (temp=0) if not provided by user 
        candidate_answers - generated responses given the question (original + perturbed)
        temperature - [0,1] for LLM randomness

        Outputs:
        score - inconsistency score (hallucination metric) 
        sc_output - specific score for each candidate answers compared with the target answer  
        '''

        if target_answer is None:
            raise ValueError("Target answer cannot be None. ")

        sc_output = []  
        target_pair = 'Q:' + question + '\nA:' + target_answer
        num_candidate_answer = len(candidate_answers)
        for i in range(num_candidate_answer): 
            candidate_pair = 'Q:' + question + '\nA:' + candidate_answers[i]
            prompt = self.prompt_temp + '\nThe first QA pair is:\n' + target_pair + '\nThe second QA pair is:\n' + candidate_pair
            res = llm_models.call_openai_model(prompt, self.model, temperature) # openai model call 
            guess = res.split(':')[1].split('\n')[0].strip()
            # print(res, guess)
            value = 0 if guess == 'Yes' else 1
            # print('value',value)
            sc_output.append(value)
        
        score = sum(sc_output)/num_candidate_answer
        return score, sc_output
    
