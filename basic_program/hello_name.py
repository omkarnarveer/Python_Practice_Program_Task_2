"""2.WAP to print “Hello Your Name” """

class Hello: #Created a class Hello

	def __init__(self,name):	#Created Prametrized Constructor
		self.name = name
	
	def show(self):  	#Funcion declaration
		print("Hello",self.name)

s=Hello("Omkar Narveer")  #object of class created
s.show() #function call
		
