'''Accept the month number and print its name and number of days in it.'''
class Calender:
	def Month(self):
		ch=int(input("Enter Month Number: "))
		if ch==1:
			print('January','31 Days')
		elif ch==2:
			print('February', '28 Days and 29 Days in Leap year')
		elif ch==3:
			print('March', '31 Days')
		elif ch==4:
			print('April', '30 Days')
		elif ch==5:
			print('May','31 Days')
		elif ch==6:
			print('June','30 Days')
		elif ch==7:
			print('July','31 Days')
		elif ch==8:
			print('August','31 Days')
		elif ch==9:
			print('September','30 Days')
		elif ch==10:
			print('October','31 Days')
		elif ch==11:
			print('November','30 Days')
		elif ch==12:
			print('December''31 Days')
		else:
			print("Wrong Choice Try again!!!")
c=Calender()
c.Month()
