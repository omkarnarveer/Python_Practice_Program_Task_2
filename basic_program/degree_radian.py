'''Write a Python program to convert degree to radian.'''
class Radian:
	def Calculate(self):
		print("Enter Degree:")
		d = float(input())
		r = d*(3.14/180)
		print("Radian of Degree:",d,"is: ",r)
c=Radian()
c.Calculate()
