'''Write a Proram to handle the exception of division of numbers.'''
class Calculate:#Class created
	print("Enter Values for Division: ")
	def __init__(self, a, b):#parameter constuctor
		self.a = a
		self.b = b
	def division(self):#funciion define
		try:
			return self.a / self.b
		except ZeroDivisionError: #exception handelled
			return "Cannot Divide by 0, Try Again."       
while True:
    print("\n************MENU************")
    print("1.Perform Division")
    print("2.Exit")
    print("*****************************")
    ch=int(input("\nEnter Choice:"))
    if ch==1:
        c = Calculate(int(input("Enter a: ")),int(input("Enter b: ")))
        show = c.division() #function call
        print("Division is:", show)
    elif ch==2:
        print("Program Ended: ")
        exit(0)
    else: print("Wrong Choice Try Again!!!\n")
