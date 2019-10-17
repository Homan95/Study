#Count
s='asdasdas sada sada sada adsasd sada sadas asdasd asdasd'
word='sada'
b=s.split()
s=0
for a in b:
	if a==word:
		s=s+1
print (s)
#Remove duplicates
a=[1,1,2,3,3,2,2]
b=[]
for i in range(len(a)):
	if not(a[i] in b):
		b.append(a[i])
print(b)
#Digits sum
a=122123
s=0
while 10//a==0:
	s=s+a%10
	a=a//10
s=s+a
print(s)

#Factorial
a=4
b=1
while a!=0:
	b=a*b
	a=a-1
print(b)
#List
b=[]
k=[]
for z in range(1,11):
	b.append(z*z)
	if z*z%2==1:
		k.append(z*z)
print(b)
print(k)
#List2
i=0
j=0
a=[]
for i in range(1,11):
	t=(i,i*i)
	a.append(t)

print(a)

