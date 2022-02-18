'''Write a Program to read a file'''
class File:  #Created Class	
	def file(self):#Function Defination to write file
		f = open("input.txt", "a+")#Opening file in write mode
		f.write("\r\n") 
		f.write(input("Enter the content to add in file:"))
		f.close()# file close
o=File() #object of class
o.file() #function call
