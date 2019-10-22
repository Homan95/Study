b=[]
def hw(a,*b):
	s=0
	
	for bb in b:
		if a=='+':
			s=s+bb
		elif a=='-':
			if b[0]==bb:
				s=b[0]
				continue
			s=s-bb
		elif a=='*':
			if b[0]==bb:
				s=b[0]
				continue
			s=bb*s
		elif a=="/":
			if b[0]==bb:
				s=b[0]
				continue
			s=s/bb
	return s

print(hw('/',12,6,3))