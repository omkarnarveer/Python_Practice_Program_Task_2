'''WAP to demonstrate use of logical operators (numeric as well as str object) '''
class Logical:
	def numeric(self):
		i=int(input("Object Value 1 for numeric:"))
		j=int(input("Object Value 2 for numeric:"))
		while True:
			ch=str(input("Enter any Logical operation 'and' 'or' 'not'  Else Press any Key to exit loop:\n"))
			if ch=='and':
				print("AND is: ",i and j)
			elif ch=='or':
				print("OR  is: ",i or j)
			elif ch=='not':
				print("Not is: ", not j)
			else:
				print("Wrong Choice Try again!!!")
				break
	def string(self):
		i=str(input("Object Value 1 for String:"))
		j=str(input("Object Value 1 for String:"))
		while True:
			ch=str(input("Enter any Logical operation 'and' 'or' 'not'  Else Press any Key to exit loop:\n"))
			if ch=='and':
				print("AND is: ",i and j)
			elif ch=='<':
				print("OR  is: ",i or j)
			elif ch=='>=':
				print("NOT is: ",not j)
			else:
				print("Wrong Choice Try again!!!")
				break
			
c=Logical()
while True:
	d=str(input("Enter choice 1 for numeric and 2 for string Else Press any Key to exit Program:\t"))
	if d=='1':
		c.numeric()
	elif d=='2': 
		c.string()
	else:
		print("Program Ended")
		exit()
