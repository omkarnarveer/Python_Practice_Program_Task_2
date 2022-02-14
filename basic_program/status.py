'''Accept Marital status  and print Miss or Mrs in front of name.'''
class Status:
	def check(self):
			a=str(input("Enter Name: "))
			b=str(input("Enter Maratal Status If Married Type 'y' if not then type 'n': "))
			if b=='y' or b=='Y':
				print("Mrs.",a)
			elif b=='n' or b=='N':
				print("Miss.",a)
			elif b!='n' or b!='N' or b!='Y' or b!='y':
				print("Wrong Choice Try Again!!!")				
			else:
				print("Wrong Choice Try Again!!!")
				print("Program Ended!!")
				exit(0)
o=Status()
o.check()
	
