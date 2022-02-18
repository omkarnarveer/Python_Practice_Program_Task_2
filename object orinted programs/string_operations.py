'''Write a python program that accepts a string from user and perform following string operations- 
i. Calculate length of string 
ii. String reversal
iii. Equality check of two strings 
iV. Check palindrome 
V. Check substring'''

class String: #class created
	
	def Input(self):#function define input
		s1=str(input("\nEnter First String: "))
		s2=str(input("Enter Second String: "))
	
	def Length(self):#function define length
		s1=str(input("\nEnter First String: "))
		s2=str(input("Enter Second String: "))
		print("\nLength of First String is",s1,": ",len(s1))
		print("Length of Second String is",s1,": ",len(s2))
	
	def Reverse(self):#function define reverse
		s1=str(input("\nEnter First String: "))
		s2=str(input("Enter Second String: "))
		print("\nReverse of String is",s1,": ",s1[::-1])
		print("Reverse of String is",s2,": ",s2[::-1])
	
	def Equal(self):#function define equal
		s1=str(input("\nEnter First String: "))
		s2=str(input("Enter Second String: "))
		print("\nEquality:",s1==s2)
	
	def Palindrome(self):#function define palindrome
		s1=str(input("\nEnter First String: "))
		s2=str(input("Enter Second String: "))
		print("\nPalindrome Status  of First String:",s1==s1[::-1])
		print("Palindrome Status  of Second String:",s2==s2[::-1])
	
	def Substring(self):#function define substrign
		s1=str(input("\nEnter First String: "))
		s2=str(input("Enter Second String: "))
		print("\nSub String Status: ",s2 in s1)
	
	def Quit(self):#function define Quit
		print("\nProgram Ended by User\n " )
		exit(0)
	
	def default(self):#function define default
		print("Wrong Choice Try Again!!!")

o=String() #object created

while True:	
	print("\n***************MENU***************")
	print("1.Calculate Length of String: ")
	print("2.String Reversal")
	print("3.Equality check of two strings")
	print("4.Check palindrome")
	print("5.Check Substring")
	print("6.Exit")
	print("**********************************\n")
	
	ch=int(input("Enter Your Choice '(''1' '2' '3' '4' '5' '6' ')': "))
	
	if ch==1:
		o.Length() #function  call
	
	elif ch==2:
		o.Reverse() #function  call
	
	elif ch==3:	
		o.Equal() #function  call
	
	elif ch==4:	
		o.Palindrome() #function  call
	
	elif ch==5:	
		o.Substring() #function  call
	
	elif ch==6:
		o.Quit() #function  call
	
	else:
		o.default()	#function  call
