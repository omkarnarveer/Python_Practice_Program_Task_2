'''To accept a number from user and print digits of number in a reverse order.'''
class Reverse:# class created
	def Number(self):#function defined
		n=int(input("Enter number: "))
		rev=0
		while(n>0):
			dig=n%10
			rev=rev*10+dig
			n=n//10
		print("Reverse of the number:",rev)
r=Reverse()#object created
r.Number()#function call
