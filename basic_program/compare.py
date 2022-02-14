''' WAP to find the largest among 3 numbers.'''

class Compare:
	def Largest(self):
		a=float(input("Enter First Number: "))
		b=float(input("Enter Second Number: "))
		c=float(input("Enter Third Number: "))
		if a>=b>=c or a>=c>=b:
			print("Largest Number is: ",a)
		elif b>=c>=a or b>=a>=c:
			print("Largest Number is: ",b)
		elif c>=b>=a or c>=a>=b:
			print("Largest Number is: ",c)
		
o=Compare()
o.Largest()
			
