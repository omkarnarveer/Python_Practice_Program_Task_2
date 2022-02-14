''' Write a Python program to calculate surface area and volume of a cylinder.'''
class Cylinder:
	def surfacearea(self):
		r=float(input("Enter Radius of Cylinder: "))
		h=float(input("Enter Vertical Height of Cylinder: "))
		area=(20*(3.14)*(r)*(h)+(2)*(3.14)*(r**2))
		print("Area of Cylinder is: ",area)
	def volume(self):
		r=float(input("Enter Radius of Cylinder: "))
		h=float(input("Enter Vertical Height of Cylinder: "))
		vol=(3.14)*(r**2)*(h)
		print("Volume of Cylinder is: ",vol)
o=Cylinder()
o.surfacearea()
o.volume()
