'''Write a program to demonstrate that a single variable can store different type of values at different instance of time'''

class Type:
	def values(self):
		a = 10
		print("Variable A:", a,type(a))
		a = 22.4
		print("Variable A:", a,type(a))
		a = 'Omkar'
		print("Variable A:", a,type(a))

o=Type()
o.values()
