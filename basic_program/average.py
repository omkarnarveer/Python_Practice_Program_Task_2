'''WAP to calculate average of three numbers.Accept numbers  from user'''
class Accept:
	def average(self):
		print("Enter three numbers: ")
		x=float(input("Enter Value for x:"))
		y=float(input("Enter Value for y:"))
		z=float(input("Enter Value for z:"))
		c=(x+y+z)/3
		print("Average of theree numbers is:",c)
o=Accept()
o.average()
