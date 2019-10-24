import json
import random
with open('questions.json') as abc:
	data=abc.read()
	questions=json.loads(data)

# Check amount of answers
a=[]
for k in range(1,20):
	a.append(0)
	for i in questions:
		if len(i['choices'])==k :
			a[k-1]+=1
print(a)

symb=['а', 'б', 'в', 'г', 'А', 'Б', 'В', 'Г', 'q']

def render_quest(qu,a):
	print (qu[a]['content'])
	for q in qu[a]['choices']:
		print(q["content"])

def rnd():
	return random.randint(0,len(questions)-1)
a=rnd()


print('Привіт, дай відповідь на питання')

render_quest(questions,a)

def asd():
	if len(questions[a]['choices'])==4:
		wasd=input('Правильний варіант а, б, в чи г? ')
	else:
		wasd=input('Правильний варіант а, б, в, г чи д? ')
	while wasd not in symb:
		print('Не правитьний ввід данних')
		wasd=input()
	if wasd=='q':
			exit(0)
	elif wasd=='а' or wasd=='А':
		qwe=0
	elif wasd=='б' or wasd=='Б':
		qwe=1
	elif wasd=='в' or wasd=='В':
		qwe=2
	elif wasd=='г' or wasd=='Г':
		qwe=3
	elif wasd=='д' or wasd=='Д':
		qwe=4
	return qwe
k=asd()


while questions!=[]:
	if questions[a]['choices'][k]['is_correct']:
		print('Молодець')
		print()
		print('Наступне питання')
		print()
		del questions[a]
		if questions==[]:
			exit(0)
		a=rnd()
		render_quest(questions,a)
		k=asd()
	else:	
		print()
		print('Спробуй заново')
		print()
		render_quest(questions,a)
		k=asd()