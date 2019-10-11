a=[i for i in range(1,101)]
b=[]
for i in range(100):
	if a[i]%7==0 and a[i]%5!=0 :
		b.append(a[i])
print(b)