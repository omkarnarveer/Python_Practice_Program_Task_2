'''WAP to demonstrate use of arithmetic operators (numeric as well as str object)'''

class Operator:
	def numeric(self):
		i=int(input("Object Value 1 for numeric:"))
		j=int(input("Object Value 2 for numeric:"))
		while True:
			ch=str(input("Enter any Arithmetic operation '+' '-' '*' '/' '//' '%' '**' Else Press any Key to exit loop:\n"))
			if ch=='+':
				print("Addition is: ",i+j)
			elif ch=='-':
				print("Subtraction is: ",i-j)
			elif ch=='*':
				print("Multiplication is: ",i*j)
			elif ch=='/':
				print("Division is: ",i/j)
			elif ch=='//':
				print("Floor Division is: ",i//j)
			elif ch=='%':
				print("Modulo is: ",i%j)
			elif ch=='**':
				print("Exponential is: ",i**j)
			else:
				print("Wrong Choice Try again!!!")
				break
	def string(self):
		i=str(input("Object Value 1 for String:"))
		j=str(input("Object Value 1 for String:"))
		while True:
			ch=str(input("Enter Arithmetic operation '+' to concatinate and '*' to Multilply String Else Press any Key to exit loop:\n"))
			if ch=='+':
				print("Concatination is",i+j)
			elif ch=='*':
				k=int(input("Enter how many times to Multiply String:"))
				print("Multiplication of Value 1 is: ",i*k,"\nMultiplication of Value 2 is: ",j*k)
			else:
				print("Wrong Choice Try again!!!")
				break
			
c=Operator()
while True:
	d=str(input("Enter choice 1 for numeric and 2 for string Else Press any Key to exit Program:\t"))
	if d=='1':
		c.numeric()
	elif d=='2': 
		c.string()
	else:
		print("Program Ended")
		exit()
