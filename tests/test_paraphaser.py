from sac3 import paraphraser

# input information - user question and target answer 
question = 'Which city is the capital of Maryland?'

# question pertubations
gen_question = paraphraser.paraphrase(question, number = 5, model = 'gpt-3.5-turbo', temperature=1.0)

print('Original question', question)
print('Generated questions', gen_question)