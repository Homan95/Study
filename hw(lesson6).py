#Fibonachi
a=10
z1=0
z2=0
res=0
for i in range(a):
	if i==0 :
		z1=0
		print(z1)
		continue
	if i==1 :
		z2=1
		print(z2)
		continue
	res=z2+z1
	z1=z2
	z2=res
	print(res)
#squared values of integers
a=[]
for i in range (1,101):
	a.append(i*i)
print(a)
# prompts the user to input the name of a car
b=[]
while not "q" in a:
	a=input('enter name of car ')
	b.append(a)
print(f'list of names: {b}')
# reverse print
a=[1,2,3,4,5,6,7,8,9,10]
z=[]
for i in range(len(a)):
	z.append(a[-i-1])
	print(a[-i-1])
print(z)