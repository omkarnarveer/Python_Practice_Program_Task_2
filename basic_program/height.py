'''Categorize the person depending on the height.
a. <150	Dwarf
b. =150 	Average heighted
c. >=165	Tall'''

class Person:
	def height(self):
		h=float(input("Enter Height of Person: "))
		if h==150:
			print("Person having Average height: ",h)
		elif h>=165:
			print("Persion having Tall height: ",h)
		elif h<150:
			print("Persion having Dwarf height: ",h)
		else:
			print("Wrong Choice Try Again!!!")
o=Person()
o.height()

