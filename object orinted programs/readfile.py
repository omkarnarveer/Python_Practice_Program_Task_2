'''Write a Program to read a file'''
class File: #Created Class	
	def file(self): #Function Defination to read file
		f = open("input.txt", "r") #Opening file in read mode
		print(f.read())# printing content of file on output screen
		f.close() # file close
o=File() #object of class
o.file() #function call
