#ЗАДАЧА 1:
#Написати функцію, яка друкує усі унікальні значення в словнику. Приклад вхідних даних: [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"}, {"VIII":"S007"}]
a=[{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"}, {"VIII":"S007"}]

def funk1(z):

	k=[]
	for i in z:
		if not(list(i.values()) in k): 
			k.append(list(i.values()))
	print(k)
funk1(a)

#ЗАДАЧА 2:Написати функцію, яка перетворює рядок в словник, де ключ - буква, а значення - її кількість в рядку.
#Наприклад, з вхідними даними : 'beetrootacademy'
#Очікується: {'a': 2, 'b': 1, 'c': 1, 'd': 1, 'e': 3, 'm': 1, 'o': 2, 'r': 1, 't': 2, 'y': 1}

a='beetrootacademy'
def funk2(z):
	k={}
	for i in z:
		if i not in list(k.keys()):
			k[i]=1
		else:
			k[i]+=1	
	k=sorted(k.items())
	print(dict(k))
funk2(a)

#ЗАДАЧА 3:Розробити функцію counter(a, b),
#Яка приймає 2 аргументи -- цілі невід'ємні числа a та b, та повертає число -- кількість різних цифр числа b, які містяться у числі а.
#Наприклад: Виклик функції: counter(12345, 567) Повертає: 1
#Виклик функції: counter(1233211, 12128) Повертає: 2
#Виклик функції: counter(123, 45) Повертає: 0

def funk3(a,b):
	a=str(a)
	b=str(b)
	s=0
	l=[]
	l1=[]
	for z in a:
		if z not in l:
			l.append(z)
	for x in b:
		if x not in l1:
			l1.append(x) 
	for i in l:
		if i in l1:
			s=s+1
	print(s)

funk3(1233211, 12128)

#ЗАДАЧА 4: Написати програму-гру, яка вміє загадувати натуральне число від 1 до 100. Програма повинна загадати число, та запитувати у користувача правильну відповідь,
#поки він не відгадає, обмеживши 10 спробами. На кожній ітерації писати - "Холодно" (Модуль різниці - більший 15), "Тепло" (Модуль різниці - від 5 до 15),
# або "Гаряче" (Модуль різниці - менший 5), в залежності від того, на скільки користувач близький до відповіді. Приклад:
#> Відгадай число від 1 до 100:
#Число: 50
#> Холодно
#Число: 25
#> Тепло
#Число: 30
#> Тепло
#Число: 35
#> Холодно
#Число: 20
#> Гаряче
#Число: 18
#> Ви вгадали!
import random
a=random.randint(1,100)
print('Відгадай число від 1 до 100:')

def enter_val():
	b=input('Число: ')
	while 1:
		if not b.isdigit():
			b=input(f'Введіть Число а не "{b}" ')
		elif int(b)>100 or int(b)<1:
			b=input(f'Введіть Число в діапазоні 1-100 ')	
		else:
			return int(b)

print(a)
for i in range(1,11):
	h=enter_val()	
	if a==h:
		print(f'Ви вгадали з {i} спроби!')
		exit(0)
	elif abs(h-a)<5:
		print('Гаряче')
	elif abs(h-a)<15:
		print('Тепло')
	else:
		print('Холодно')
print(f'ви вичерпали всі спроби, загадане число {a}')

#Write a Python function that takes two lists and returns True if they have at least one common member.
def funk4(a,b):
	for i in a:
		if i in b:
			return True
	return False
#Write a Python function to shuffle and print a specified list. [1, 2, 3, 4, 6] -> [3, 2, 4, 5, 1]
def funk5(a):
	z=[]
	while a!=[]:
		z.append(a.pop(random.randint(0,len(a)-1)))
	print(z)
funk5([1, 2, 3, 4, 6])

#Write a Python function to get first, second best scores from the list.
#List may contain duplicates.
#Ex: [86,86,85,85,85,83,23,45,84,1,2,0] => should get 86, 85
aa=[86,86,85,85,85,83,23,45,84,1,2,0]
def funk6(a):
	k1=0
	k2=0
	for i in a:
		if i>k1:
			k1=i
		elif i>k2 and k1!=i:
			k2=i
	print (k1, k2)
funk6(aa)
#{'Student': 10, 'student1': 20, 'student3': 30}
#Get first and second best scores students
aa={'Student': 10, 'student1': 20, 'student3': 30}
def funk7(a):
	k1=0
	k2=0
	z1=''
	z2=''
	for i in list(a.keys()):
		if a[i]>k1:
			k2=k1
			z2=z1
			k1=a[i]
			z1=i
		elif a[i]>k2:
			k2=a[i]
			z2=i
	print ({z1:k1,z2:k2})
funk7(aa)

#Write a Python function to display products with price less or equal form user input 
products = {
'SMART WATCH': 550,
'PHONE' : 1000,
'PLAYSTATION': 500,
'LAPTOP' : 1550,
'MUSIC PLAYER' : 600,
'TABLET' : 400
}

a=int(input('enter value '))
def funk8(a,b):
	for i in list(a.keys()):
		if a[i]<=b:
			print(i)
funk8(products,a)