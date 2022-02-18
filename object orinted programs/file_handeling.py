'''Wrie a Progam To copy contents of one file to other. 
While copying a) all full stops are to be replaced with commas b) lower case are to be replaced with upper case 
c) upper case are to be replaced with lower case.'''
class File:# class created
	def read_write_copy(self): #function creared
		try:
			fin = open("input.txt",'a+')
			for i in range(10):
				fin.write("This file is created by. omkar narveer. Using Python \r\n")   # file opening in read mode
			fin.close()
			with open('input.txt','r') as fin, open('output.txt','w') as fout:
				for line in fin:
					line = line.swapcase()   #Replace lower case with upper and upper with lower
					line = line.replace(".",",")  #Replace full stops with ,
					fout.write(line)
			fin.close()
							 
		except:
			print("File error occured")
		 
o=File()#object
o.read_write_copy()#function call
