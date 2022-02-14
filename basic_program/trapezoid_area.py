'''Write a Python program to calculate the area of a trapezoid.'''
class Trapezoid:
	def area(self):
		tb=float(input("Enter Top Base of Trapezoid: "))
		bb=float(input("Enter Bottom Base of Trapezoid: "))
		vh=float(input("Enter Vertical Height of Trapezoid: "))
		area=((tb+bb)/2)*vh
		print("Area of Trapezoid is: ",area)
o=Trapezoid()
o.area()
