'''1.Write a Program to print following to Output Screen
	Escape character		Use
	\n			Newline
	\t			Space/tab
	\'			Single Quote
	\"			Double Quote'''
'''print("Escape Character\t\t","Use")
print("\t\\n","\t\tNewline")
print("\t\\t","\t\tSpave/tab")
print("\t\\'","\t\tSingle Quote")
print('\t\\"',"\t\tDouble Quote")
#OR'''
class Escape:
	def display(self):
		print("{}  {}". format("Escape Character","\t\tUse"))
		print("{}  {}". format("\t\\n","\t\t\tNewline"))
		print("{}  {}". format("\t\\t","\t\t\tSpave/tab"))
		print("{}  {}". format("\t\\'","\t\t\tSingle Quote"))
		print("{}  {}". format('\t\\"',"\t\t\tDouble Quote"))
d=Escape()
d.display()
