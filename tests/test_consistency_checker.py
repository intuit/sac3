from sac3 import paraphraser
from sac3.evaluator import Evaluate
from sac3.consistency_checker import SemanticConsistnecyCheck

# input information
question = 'Was there ever a US senator that represented the state of Alabama and whose alma mater was MIT?'
target_answer = 'Never'

# question pertubation
gen_question = paraphraser.paraphrase(question, number = 3, model = 'gpt-3.5-turbo', temperature=1.0)

# llm evaluation
llm_evaluate = Evaluate(model='gpt-3.5-turbo')
self_responses = llm_evaluate.self_evaluate(self_question = question, temperature = 1.0, self_num = 3)
perb_responses = llm_evaluate.perb_evaluate(perb_question = gen_question, temperature=0.0)

# consistency check 
scc = SemanticConsistnecyCheck(model='gpt-3.5-turbo')

sc2_score, sc2_vote = scc.score_scc(question, target_answer, candidate_answer = self_responses, temperature = 0.0)
print(sc2_score, sc2_vote)

sac3_q_score, sac3_q_vote = scc.score_scc(question, target_answer, candidate_answer = perb_responses, temperature = 0.0)
print(sac3_q_score, sac3_q_vote)