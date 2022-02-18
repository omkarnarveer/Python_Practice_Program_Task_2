'''To accept an object mass in kilograms and velocity in meters per second and display its momentum. Momentum is calculated as e=mc 2 where m is the mass of the object and c is
its velocity.'''

class Momentum:	#class created
	def formula(self,m,c):#function defination
		print('Momentum is: ',((m)*(c**2)))
	
e=Momentum()#object created
e.formula(10,3)#int function call
e.formula(2.6,3.2)#float function call
e.formula(float(input("Enter Mass of object: ")),float(input("Enter Veocity of Object: ")))#user input funtion call
