'''Accept name,age and address from user and display it as ( You are allowed to use only 1 print())
Name:Username
Age:Userage
Address:UserAddress'''

class Display:
	def accept(self):
		n= input("Enter Username: ")
		ag=input("Enter Userage: ")
		ad=input("Enter UserAddress: ")
		print("\n Username:",n,"\n","Userage:",ag,"\n","UserAddress:",ad)
		
o=Display()
o.accept()
