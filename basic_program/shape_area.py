'''Write a Menu driven program for following
 Area of circle (pi*r²)
 Area of Rectangle (l*b)
 Area of triangle (b*h/2)
 Area of Square (a²)'''
class Menu:
	def Circle(self):
		print("Enter Radius: ")
		r=float(input())
		a=(3.14)*(r**2)
		print("\nArea of Circle is:",a)

	def Rectangle(self):
		print("Enter Length: ")
		l=float(input())
		print("Enter Breadth: ")
		b=float(input())
		a=l*b
		print("\nArea of Rectangle is:",a)
	
	def Triangle(self):
		print("Enter Base: ")
		b=float(input())
		print("Enter Vertical Height: ")
		h=float(input())
		a=((b*h)/2)
		print("\nArea of Triangle is:",a)
		
	def Square(self):
		print("Enter Length: ")
		l=float(input())
		a=(l**2)
		print("\nArea of Square is:",a)
	
	def ex(self):
		exit(0)
	
	def default(Self):
		print("Wrong Choice Try Again!!!")	
o=Menu()
while True:
	print("\n**********MENU**********")
	print("1.Area of Circle")
	print("2.Area of Rectangle")
	print("3.Area of Triangle")
	print("4.Area of Square")
	print("5.Exit")
	print("************************")
	ch=int(input("\nEnter Choice: "))
	if ch==1:
	    o.Circle()
	elif ch==2:
		o.Rectangle()
	elif ch==3:
		o.Triangle()
	elif ch==4:
		o.Square()
	elif ch==5:
		o.ex()
	else:
		o.default()
