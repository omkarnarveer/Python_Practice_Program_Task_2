'''Write a Python program to calculate the area of a parallelogram.'''
class Parallelogram:
	def area(self):
		b=float(input("Enter Base of Parallelogram: "))
		
		h=float(input("Enter Vertical Height of Parallelogram: "))
		area=b*h
		print("Area of Parallelogram is: ",area)
o=Parallelogram()
o.area()
