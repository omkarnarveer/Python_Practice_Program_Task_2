'''WAP to demonstrate use of assignment operators (numeric as well as str object)'''
class Operator:
	def numeric(self):
		i=int(input("Object Value 1 for numeric:"))
		j=int(input("Object Value 2 for numeric:"))
		while True:
			ch=str(input("Enter any Assignment operation '=' '+=' '-=' '*=' '/=' '%=' '**=' '&=' '|=' '^=' '>>=' '<<='  Else Press any Key to exit loop:\n"))
			if ch=='=':
				print("Equals to:",i=j)
			elif ch=='+=':
				print("Plus Equal to",i += j)
			elif ch=='-=':
				print("Minus Equal to",i-=j)
			elif ch=='*=':
				print("Multiplication Equals to",i*=j)
			elif ch=='/=':
				print("Division Equals to",i/=j)
			elif ch=='%=':
				print("Modulo Equals to",i%=j)
			elif ch=='**=':
				print("Exponential Equal to: ",i**=j)
			elif ch=='|=':
				print(" Bitwise OR: ",i|=j)
			elif ch=='&=':
				print("Bitwise AND: ",i&=j)
			elif ch=='^=':
				print("Bitwise EXOR: ",i^=j)
			elif ch=='>>=':
				print("Bitwise Right Shift: ",i>>=j)
			elif ch=='<<=':
				print("Bitwise Left Shift: ",i<<=j)
			else:
				print("Wrong Choice Try again!!!")
				break
	def string(self):
		i=str(input("Object Value 1 for String:"))
		j=str(input("Object Value 1 for String:"))
		while True:
			ch=str(input("Enter any Assignment operation '=' '+=' '-=' '*=' '/=' '%=' '**=' '&=' '|=' '^=' '>>=' '<<='  Else Press any Key to exit loop:\n"))
			if ch=='=':		
				print("Equals to:", k=j)
			elif ch=='+=':
				print("Plus Equal to",i+=j)
			elif ch=='-=':
				print("Minus Equal to",i-=j)
			elif ch=='*=':
				print("Multiplication Equals to",i*=j)
			elif ch=='/=':
				print("Division Equals to",i/=j)
			elif ch=='%=':
				print("Modulo Equals to",i%=j)
			elif ch=='**=':
				print("Exponential Equal to: ",i**=j)
			elif ch=='|=':
				print(" Bitwise OR: ",i|=j)
			elif ch=='&=':
				print("Bitwise AND: ",i&=j)
			elif ch=='^=':
				print("Bitwise EXOR: ",i^=j)
			elif ch=='>>=':
				print("Bitwise Right Shift: ",i>>=j)
			elif ch=='<<=':
				print("Bitwise Left Shift: ",i<<=j)
			else:
				print("Wrong Choice Try again!!!")
				break
			
c=Operator()
while True:
	d=int(input("Enter choice 1 for numeric and 2 for string Else Press any Key to exit Program:\t"))
	if d==1:
		c.numeric()
	elif d==2: 
		c.string()
	else:
		print("Program Ended")
		exit()
