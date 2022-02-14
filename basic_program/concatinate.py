'''Write a program to concatenate two strings.'''
class Concatinate:
	global s1 ,s2 ,s3
	def Join(self):
		s1=str(input("Enter First string:"))
		s2=str(input("Enter Second string:"))
		s3=s1+ s2
		print('Concatinated String is: ',s3)
j=Concatinate()
j.Join()
