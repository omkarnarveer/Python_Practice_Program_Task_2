'''WAP to calculate x raised to the power n (xn). Accept the value of x and n from the user.'''
class Exponential:
	def calculate(self):
		print("Calulate Value for 'x' to the power 'n'")
		x=int(input("Enter Value of x: "))
		n=int(input("Enter Value of n: "))
		c=x**n
		print("Calulated Value for ",x ,"to the power",n , "is: ",c)
o=Exponential()
o.calculate()
