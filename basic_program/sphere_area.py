'''Write a Python program to calculate surface area and volume of a sphere'''
class Sphere:
	def surfacearea(self):
		r=float(input("Enter Radius of Sphere: "))
		area=((4)*(3.14)*(r**2))
		print("Area of Cylinder is: ",area)
	def volume(self):
		r=float(input("Enter Radius of Sphere: "))
		vol=(4/3)*(3.14)*(r**3)
		print("Volume of Sphere is: ",vol)
o=Sphere()
o.surfacearea()
o.volume()
