'''WAP to check if a candidate is eligible for voting or not.'''
class Candidate:
	def check(self):
		n=str(input("Enter Candidate Name: "))
		a=int(input("Enter Age of Candidate: "))
		if a>=18:
			print(n,"is Eligible to Vote.")
		else:
			print(n,"is not Eligible to Vote.")
o=Candidate()
o.check()
