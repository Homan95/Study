a=input('enter operation, + - * / is available for now ').strip()

if a=='+' or a=='-' or a=='*' or a=='/' :
	b=input('enter your 1 value ').strip()
	
	if not b.isdigit() and not b.replace('.','',1).isdigit() and not b.lstrip('-').isdigit() and not b.lstrip('-').replace('.','',1).isdigit():
		b=input('error! enter your 1 value ')
		if not b.isdigit() and not b.replace('.','',1).isdigit() and not b.lstrip('-').isdigit() and not b.lstrip('-').replace('.','',1).isdigit():
			print('You are dump') #якби можна було б виористати goto тоді б ця перевірка була б нескінченною
			exit(0)
	b=float(b)

	c=input('enter your 2 value ').strip()
	
	if not c.isdigit() and not c.replace('.','',1).isdigit() and not c.lstrip('-').isdigit() and not c.lstrip('-').replace('.','',1).isdigit():
		c=input('error! enter your 2 value ')
		if not c.isdigit() and not c.replace('.','',1).isdigit() and not c.lstrip('-').isdigit() and not c.lstrip('-').replace('.','',1).isdigit():
			print('You are dump')
			exit(0)
	c=float(c)
	
	if a=='+' :
		d=b+c;
	if a=='-' :
		d=b-c;
	if a=='*' :
		d=b*c;
	if a=='/' :
		if c==0 :
			print('error - DIV/0')
			exit(0)
		else :
			d=b/c;
	
	print ('Result', b, a, c, '=', d)
else :
	print('operation "',a,'" is not supported for now')