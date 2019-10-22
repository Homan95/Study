import random

questions = [
    {
        "content": "2 + 2 - 4 = ",
        "choices": [
            {"content": "0", "is_correct": True},
            {"content": "24", "is_correct": False},
        ],
    },
    {
        "content": "18 / 2 = ",
        "choices": [
            {"content": "5", "is_correct": False},
            {"content": "9", "is_correct": True},
        ],
    },
]
print('Hello, pls do some math')

def rnd():
	return random.randint(0,len(questions)-1)
a=rnd()

def asd():
	print(f"{questions[a]['content']}")
	print('your options (p.s. type 1 or 2 to check answer)')
	for i, zz in enumerate(questions[a]['choices']):
		print(f"{i+1}. {zz['content']}")		
	wasd=input()
	
	while wasd!='1' and wasd!='2':
		print('Error - pls type only 1 or 2')
		wasd=input()
		

	return wasd
k=asd()

while questions!=[]:
	if questions[a]['choices'][int(k)-1]['is_correct']:
		print('well done')
		del questions[a]
		if questions==[]:
			exit(0)
		a=rnd()
		k=asd()
	else:	
		print('try again')
		k=asd() 