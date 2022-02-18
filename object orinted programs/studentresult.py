'''To accept student’s five courses marks and compute his/her result. Student is passing if
he/she scores marks equal to and above 40 in each course. If student scores aggregate
greater than 75%, then the grade is distinction. If aggregate is 60>= and <75 then the
grade if first division. If aggregate is 50>= and <60, then the grade is second division. If
aggregate is 40>= and <50, then the grade is third division.'''

class Student: # Class Created
	def Subject(self):# function
		m1=int(input("Enter the Marks in Engineering Mathematics 1:"))
		m2=int(input("Enter the Marks in Programming and Problem Solving:"))
		m3=int(input("Enter the Marks in Systems in Mechanical Engineering:"))
		m4=int(input("Enter the Marks in Basic Electrical Engineering:"))
		m5=int(input("Enter the Marks in Engineering Chemistry:"))
		total=m1+m2+m3+m4+m5
		avg=float(total)/5
		print("Total of Marks:",total,"\nAverage of Marks:",avg)
		if(avg>75):
			print(" Result Is Pass With Distinction Class.")
		elif(avg>=60):
			print("Result Is Pass With First Class.")
		elif(avg>=50):
			print("Result Is Pass With Second Class.")
		elif(avg>=40):
			print("Result Is Pass Class.")
		else:
			print("Result Is Fail.")

o=Student() # Object
o.Subject()#Function Call

