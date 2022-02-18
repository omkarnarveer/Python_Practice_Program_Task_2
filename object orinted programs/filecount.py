'''Writ a Program to count total characters in file, total words in file, total lines in file and frequency of
given word in file. '''
class File: #class Created
	def file(self):#function defined
		file = open("input.txt", "r")
		number_of_lines = 0
		number_of_words = 0
		number_of_characters = 0
		for line in file:
			line = line.strip("\n")
			words = line.split()
			num_of_lines += 1
			num_of_words += len(words)
			num_of_characters += len(line)
		file.close()
		print("lines:", num_of_lines, "words:", num_of_words, "characters:", num_of_characters)
o=File()#object created
o.file()#Funcion call

