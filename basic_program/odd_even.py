'''WAP to determine input number is even or odd.'''
class Number:
	def calculate(self):
		num=float(input("Enter any Number: "))
		if num%2==0:
			print("Entered Number ",num," is Even.")
		else:
			print("Entered Number ",num," is Odd.")
o=Number()
o.calculate()
