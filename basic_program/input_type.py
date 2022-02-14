'''WAP to check type of data accepted using input() function'''
class Type:
	def values(self):
		while True:
			i=str(input("Press Y or y to Proceed else press any key to exit Program: "))
			if i=='Y'or i=='y':
				a = input("Enter Your Input: ")
				print("Input Type is:", a,type(a))
			else:
				exit("Program Exit")
o=Type()
o.values()
