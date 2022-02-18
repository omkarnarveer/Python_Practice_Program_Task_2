"""To accept two numbers from user and compute and Greatest Common
Divisor of these two numbers."""
import math #imported math module for gcd
class Numbers:# Class Created
	def GCD(self):#Function Defined
		print("The GCD of two number:")
		print(math.gcd(int(input("Enter 1st Number: ")),int(input("Enter 2nd Number: "))))
n=Numbers() #Object
n.GCD()#Function call

