'''Write a program to demonstrate single and multiple assignment of values to a variables'''
class values:
	def single(self):
		a=100
		print("Single assignmet value to Variable a:",a)
	def multiple(self):
		a=10
		print("\nMultiple assignment value to Variable a:",a)
		a=10.4
		print("Multiple assignment value to Variable a:",a)
		a='Omkar'
		print("Multiple assignment value to Variable a:",a)
o=values()
o.single()
o.multiple()
