'''Write a Prgram to print Fibonacci Series of specific number and range'''
class Fibonacci: #class created
	def Num():#funcion for number
		print("Enter the value of n:")
		n=int(input())
		a=0
		b=1
		i=0
		print("Fibonacci Value is:")
		while i<n:
			c=a+b
			a=b
			b=c
			i=i+1
		print(a)
	def Range(): #function for range
		print("Enter the Range of n:")
		n=int(input())
		a=0
		b=1
		i=0
		print("Fibonacci Sequence is:")
		while i<n:
			c=a+b
			a=b
			b=c
			i=i+1
			print(a)
d=Fibonacci #object created
d.Num()#number funcion called
d.Range()#range function called
