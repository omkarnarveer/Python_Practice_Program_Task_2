'''Use type casting to check every possibility of type casting  ( int to other types,float to other type,..).Form a table as below to maintain track.[P:Possible N=Not Possible]
Cast to→		int	float	bool	complex	str
int			            P	
float			P
bool			P
complex		N
str			             *P         '''

class Typecasting:	
	def display(self):
		print("Cast to->\tint\tfloat\tbool\tComplex\tstr")
		print("int\t\tP\tP\tP\tP\tP")
		print("float\t\tP\tP\tP\tP\tP")
		print("bool\t\tP\tP\tP\tP\tP")
		print("complex\t\tN\tN\tP\tP\tP")
		print("str\t\tN\tN\tP\tN\tP")
	
	def typeint(self):
		i=int(input("Enter Integer Value: "))	
		print(type(i))
		print(int(i))
		print(float(i))
		print(bool(i))
		print(complex(i))
		print(str(i))
	
	def typefloat(self):
		f=float(input("Enter Floating Value:"))
		print(type(f))
		print(int(f))
		print(float(f))
		print(bool(f))
		print(complex(f))
		print(str(f))

	def typebool(self):
		b=bool(input("Enter Boolean Value: "))
		print(type(b))
		print(int(b))
		print(float(b))
		print(bool(b))
		print(complex(b))
		print(str(b))

	def typecomplex(self):
		c=complex(input("Enter Complex Value: "))
		print(type(c))
		try:
			print(int(c))
		except TypeError:
			print('Cannot Typecast')
		try:    
			print(float(c))
		except TypeError:
			print('Cannot Typecast')
		print(bool(c))
		print(complex(c))
		print(str(c))

	def typestring(self):
		s=str(input("Enter String Value:"))
		print(type(s))
		try:
			print(int(s))
		except ValueError:
			print('Cannot Typecast')
		try:
			print(float(s))
		except ValueError:
			print('Cannot Typecast')
		print(bool(s))
		try:
			print(complex(s))
		except ValueError:
			print('Cannot Typecast')
		print(str(s))
		
c=Typecasting()
while True:
	print("***************MENU***************")
	print("1.Integer Typecast")
	print("2.Float Typecast")
	print("3.Boolean Typecast")
	print("4.Complex Typecast")
	print("5.String Typecast")
	print("6.Display Typecast Table")
	print("7.Exit Program")
	print("**********************************")
	ch=int(input("Enter Your Choice: "))
	if ch==1:
		c.typeint()
	elif ch==2:
		c.typefloat()
	elif ch==3:
		c.typebool()
	elif ch==4:
		c.typecomplex()
	elif ch==5:		
		c.typestring()
	elif ch==6:
		c.display()
	elif ch==7:
		print("Program Ended by User key 7")
		exit(0)
	else:
		print("Wronge Choice Try again!!!")
