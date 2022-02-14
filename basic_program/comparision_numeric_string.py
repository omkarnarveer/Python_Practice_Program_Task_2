'''WAP to demonstrate use of comparison operators (numeric as well as str object)'''
class Comparision:
	def numeric(self):
		i=int(input("Object Value 1 for numeric:"))
		j=int(input("Object Value 2 for numeric:"))
		while True:
			ch=str(input("Enter any Comparision operation '>' '<' '>=' '<=' '==' '!=' Else Press any Key to exit loop:\n"))
			if ch=='>':
				print("Greater is: ",i>j)
			elif ch=='<':
				print("Less than is: ",i<j)
			elif ch=='>=':
				print("Multiplication is: ",i>=j)
			elif ch=='<=':
				print("Less than Equal to: ",i<=j)
			elif ch=='==':
				print("Equal to: ",i==j)
			elif ch=='!=':
				print("Not Equal to: ",i!=j)
			else:
				print("Wrong Choice Try again!!!")
				break
	def string(self):
		i=str(input("Object Value 1 for String:"))
		j=str(input("Object Value 1 for String:"))
		while True:
			ch=str(input("Enter any Comparision operation '>' '<' '>=' '<=' '==' '!=' Else Press any Key to exit loop:\n"))
			if ch=='>':
				print("Greater is: ",i>j)
			elif ch=='<':
				print("Less than is: ",i<j)
			elif ch=='>=':
				print("Multiplication is: ",i>=j)
			elif ch=='<=':
				print("Less than Equal to: ",i<=j)
			elif ch=='==':
				print("Equal to: ",i==j)
			elif ch=='!=':
				print("Not Equal to: ",i!=j)
			else:
				print("Wrong Choice Try again!!!")
				break
			
c=Comparision()
while True:
	d=str(input("Enter choice 1 for numeric and 2 for string Else Press any Key to exit Program:\t"))
	if d=='1':
		c.numeric()
	elif d=='2': 
		c.string()
	else:
		print("Program Ended")
		exit()
