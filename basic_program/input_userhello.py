'''WAP to accept name from user and display'''

class Hello: #Created a class Hello

	def __init__(self,name):	#Created Prametrized Constructor
		self.name = name
	
	def show(self):  	#Funcion declaration
		print("Hello",self.name)

s=Hello(str(input("Enter Username: ")))  #object of class created
s.show() #function call
		
