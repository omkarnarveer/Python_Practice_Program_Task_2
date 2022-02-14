''' Write a program to check if a triangle is valid or not.(Input-3 angles of triangle).'''
class Triangle:
	def Angle(self):
		a1=float(input("Enter First angle of Triangle: "))
		a2=float(input("Enter Second angle of Triangle: "))
		a3=float(input("Enter Third angle of Triangle: "))
		s=a1+a2+a3
		if s==180 and a1!=0 and a2!=0 and a3!=0:
			print("Triangle is valid.")
		else:
			print("Triangle is Not valid.")
s=Triangle()
s.Angle()
