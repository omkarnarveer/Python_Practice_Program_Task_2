'''Write a program to calculate simple interest.Accept values from user.(si=pnr/100)'''
class Simple:
	def interest(self):
		p=float(input("Enter Principal value borrowed:"))
		r=float(input("Enter Rate of Interest: "))
		t=float(input("Enter time Duration in Years: "))
		si=((p*r*t)/100)
		print("Simple Interest is :",si)
c=Simple()
c.interest()
