'''Determine if the input number is positive or negative.'''

class Number:
	def check(self):
		n=float(input("Enter a Number: "))
		if n>0:
			print("Enterd Number:",n,"is Positive.")
		elif n==0:
			print("Enterd Number:",n,"is Zero.")
		else:
			print("Enterd Number:",n,"is Negative.")
o=Number()
o.check()
