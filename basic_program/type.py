'''WAP to assign different type of values to one variable at different instance of and print its type each time'''
class Type:
	def values(self):
		while True:
			i=str(input("Press Y or y to Proceed else press any key to exit Program: "))
			if i=='Y'or i=='y':
				a = input("Assign value to variable a: ")
				print("Variable A:", a,type(a))
			else:
				exit("Program Exit")
o=Type()
o.values()
