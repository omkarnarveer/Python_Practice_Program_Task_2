''' Accept Student Details-Rollno,Name,percent and display as (Use 2 print())
	Rollno		Name		Percentage
	UserRoll	Username	UserPercent   '''
class Student:
	def info(self):
		a=int(input("Enter Roll No. "))
		b=str(input("Enter Student Name: "))
		c=float(input("Enter Student Percentage:"))
		print("\nRollno","\t\t\tName","\t\t\tPercentage")
		print(a,"\t\t\t",b,"\t\t\t",c)
s=Student()
s.info()
