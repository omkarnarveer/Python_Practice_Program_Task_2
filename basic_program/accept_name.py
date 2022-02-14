''' Accept first name middle name and surname from user (Use 3 input() ).Display the user input as
Surname Firstname Middlename'''

class Display:
	def accept(self):
		print("Enter Firstname:")
		f=input()
		print("Enter Middlename:")
		m=input()
		print("Enter Surame:")
		s=input()
		print("Surname\t","Firstname\t","Midname")
		print(s,'\t',f,'\t',m);
o=Display()
o.accept()
		
