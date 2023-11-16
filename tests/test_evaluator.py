from sac3 import paraphraser
from sac3.evaluator import Evaluate
from sac3.consistency_checker import SemanticConsistnecyCheck

# input information
question = 'is pi samller than 3.2?'

# question pertubation
gen_question = paraphraser.paraphrase(question, number = 5, model = 'gpt-3.5-turbo', temperature = 1.0)

# llm evaluation
llm_evaluate = Evaluate(model='gpt-3.5-turbo')
self_responses = llm_evaluate.self_evaluate(self_question = question, temperature = 1.0, self_num = 5)
perb_responses = llm_evaluate.perb_evaluate(perb_question = gen_question, temperature = 0.0)

print('Original question', question)
print('self_responses', self_responses)
print('perb_responses', perb_responses)