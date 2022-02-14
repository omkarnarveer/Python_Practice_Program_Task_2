'''Write a Python program to convert radian to degree.'''
class Degree:
	def Calculate(self):
		print("Enter Radian:")
		r = float(input())
		d = r*(180/3.14)
		print("Degree of Radian:",r,"is: ",d)
c=Degree()
c.Calculate()
