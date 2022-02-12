"""Problem Statement: Write a Program to Calulate Area and Perimeter of Geometic Shapes.
Create user defined module for each separate Shape create a Menu driven program to call the user defined module into single main module ."""

"Solution:->"

"Importing User Defined Modules"

from Circle import Cr_Area as cra, Cr_Perimeter as crp 
from Triangle import Tr_Area as tra, Tr_Perimeter as trp
from Square import Sq_Area as sqa, Sq_Perimeter as sqp
from Rectangle import Rt_Area as rta, Rt_Perimeter as rtp
from Cube import Cu_Area as cua, Cu_Perimeter as cup
#Created  Menu Block
def menu():
	print("\n***********MENU***************")
	print(" 1.Calulate Area of Circle: ")
	print(" 2.Calulate Perimeter of Circle: ")
	print(" 3.Calulate Area of Square: ")
	print(" 4.Calulate Perimeter of Square: ")
	print(" 5.Calulate Area of Cube: ")
	print(" 6.Calulate Perimeter of Cube: ")
	print(" 7.Calulate Area of Triangle: ")
	print(" 8.Calulate Perimeter of Triangle: ")
	print(" 9.Calulate Area of Rectangle: ")
	print("10.Calulate Perimeter of Recangle: ")
	print("11.Exit ")
	print("******************************")

#Created Switch Block to Call modules as per user choice
def switch():	
	while True:
		ch=int(input("\nEnter Your Choice from 1 to 11: "))
		if ch==1:
			cra()
		elif ch==2:
			crp()
		elif ch==3:
			sqa()
		elif ch==4:
			sqp()
		elif ch==5:
			cua()
		elif ch==6:
			cup()
		elif ch==7:
			tra()
		elif ch==8:
			trp()
		elif ch==9:
			rta()
		elif ch==10:
			rtp()
		elif ch==11:
			print("Program has been Terminated By User Key 11\n")
			exit(0)
		else:
			print("!!!Wrong Choice Try Again!!!\n")

#Calling menu Function
menu()
#Calling Swtich Function
switch()
	
