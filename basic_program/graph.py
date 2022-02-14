'''WAP to accept coordinates of a point and determine in which Quadrant it lies.'''
class Graph:
	def Quadrant(self):
		x=(float(input("Enter Value of X-axis: ")))
		y=(float(input("Enter Value of Y-axis: ")))
		if x>0 and y>0:
			print("Coordinate x= ",x,"and y=",y, "Lies in First Quadrant")
		elif x<0 and y>=0:
			print("Coordinate x= ",x,"and y=",y, "Lies in Second Quadrant")
		elif x>=0 and y<0:
			print("Coordinate x= ",x,"and y=",y, "Lies in Third Quadrant")
		elif x<0 and y<0:
			print("Coordinate x= ",x,"and y=",y, "Lies in Fourth Quadrant")
		elif x==0 and y==0:
			print("Coordinate x= ",x,"and y=",y, "Lies in Origin")
		else:
			print("Wrong Choice Try Again!!!")
o=Graph()
o.Quadrant()
