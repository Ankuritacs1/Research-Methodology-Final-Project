questions = []
answers = []

def get_answer(question, options):

	questions.append(question)
	print(question)
	print('Options-----\n')
	for i,j in options.items():
		print(i + ". " + j)
	option = input('\nPlease select an option: ')

	while not option in list(options.keys()):
		print(f'\nIncorect option. Only valid A or B\n')
		print('Options-----\n')
		for i,j in options.items():
			print(i + ". " + j)
		option = input('\nPlease select an option: ')
	answers.append(options[option])
	print()




# Cost questions
ques1 = "How much is your budget?"
opts1 = {"A": "A little", "B": "A lot"}
get_answer(ques1, opts1)

ques2 = "Do you have an IT team?"
opts2 = {"A": "Yes", "B": "No"}
get_answer(ques2, opts2)


# Security questions
ques3 = "Do you have a Data Security/threat protection team?"
opts3 = {"A": "Yes", "B": "No"}
get_answer(ques3, opts3)

ques4 = 'Do you need a Data backup?'
opts4 = {"A": "Yes", "B": "No"}
get_answer(ques4, opts4)


# Deployment and Scalability questions
ques5 = "Does the Flexibility an important factor to you?"
opts5 = {"A": "Yes", "B": "No"}
get_answer(ques5, opts5)

ques6 = "Do you want a quick deployment and agile setup?"
opts6 = {"A": "Yes", "B": "No"}
get_answer(ques6, opts6)

ques7 = "Does the Scalability an important factor to you?"
opts7 = {"A": "Yes", "B": "No"}
get_answer(ques7, opts7)

ques8 = "Does the Reliability an important factor to you?"
opts8 = {"A": "Yes", "B": "No"}
get_answer(ques8, opts8)


# User access questions
ques9 = 'Do you need anywhere access (via mobile app, browser, PC) to your service?'
opts9 = {"A": "Yes", "B": "No"}
get_answer(ques9, opts9)

ques10 = 'Do you have a good internet connectivity?'
opts10 = {"A": "Yes", "B": "No"}
get_answer(ques10, opts10)

ques11 = "Do you need speed storing data?"
opts11 = {"A": "Yes", "B": "No"}
get_answer(ques11, opts11)


local = 0
cloud = 0

#Tree decision
if answers[0] == 'A little':
	cloud += 1
elif answers[0] == 'A lot':
	local += 1

if answers[1] == 'Yes':
	local += 1
elif answers[1] == 'No':
	cloud += 1

if answers[2] == 'Yes':
	local += 1
elif answers[2] == 'No':
	cloud += 1

if answers[3] == 'Yes':
	cloud += 1
elif answers[3] == 'No':
	local += 1

if answers[4] == 'Yes':
	local += 1
elif answers[4] == 'No':
	cloud += 1

if answers[5] == 'Yes':
	cloud += 1
elif answers[5] == 'No':
	local += 1

if answers[6] == 'Yes':
	cloud += 1
elif answers[6] == 'No':
	local += 1

if answers[7] == 'Yes':
	cloud += 1
elif answers[7] == 'No':
	local += 1

if answers[8] == 'Yes':
	cloud += 1
elif answers[8] == 'No':
	local += 1

if answers[9] == 'Yes':
	cloud += 1
elif answers[9] == 'No':
	local += 1

if answers[10] == 'Yes':
	local += 1
elif answers[10] == 'No':
	cloud += 1

questions.append("Recommendation")
if cloud > local:
	answers.append("Cloud Computing")
	print("I recommend you to choose the technology cloud computing")
elif cloud < local:
	answers.append("On Premise")
	print("I recommend you to choose the technology on premise")


import pandas as pd



try:
	original = pd.read_csv("survey.csv")
	df = pd.DataFrame([answers], columns =questions)
	df = pd.concat([df, original], axis=0)
	df.to_csv("survey.csv",index=False)
except:
	df = pd.DataFrame([answers], columns =questions)
	df.to_csv("survey.csv",index=False)
