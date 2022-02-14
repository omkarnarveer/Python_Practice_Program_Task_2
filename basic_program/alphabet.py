'''WAP to check if the alphabet is a vowel or consonant.'''
class Alphabet:
	def check(self):
		a=str(input("Enter an Alphabet: "))
		if a=='a' or a=='A' or a=='e' or a=='E' or a=='i' or a=='I' or a=='o' or a=='O' or a=='u' or a=='U':
			print("Entered Alphabet",a,'is Vowel.')
		else:
			print("Entered Alphabet",a,'is Consonant.')
o=Alphabet()
o.check()
