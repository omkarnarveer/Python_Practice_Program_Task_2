'''To calculate salary of an employee given his basic pay (take as input from user).
Calculate gross salary of employee. Let HRA be 10 % of basic pay and TA be 5% of
1.
basic pay. Let employee pay professional tax as 2% of total salary. Calculate net salary
payable after deductions.'''
class Employee: #class Created
	def Salary():#Function Defined
		basic=int(input("Enter the Basic Salary:$"))	
		Gross=basic+10/100*basic+5/100*basic
		net=Gross-2/100*Gross
		print("Net Salary after Deduction:$",net) 
s=Employee #object of class
s.Salary()#funcion call
