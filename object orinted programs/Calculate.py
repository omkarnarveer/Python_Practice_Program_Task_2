'''To accept N numbers from user. Compute and display maximum in list, minimum in list, sum and average of numbers.'''
class Calculate:#class Created
	def Numbers(self):#function Define
		N=int(input("How Many Numbers do you want to Calculate:"))
		data=[]
		for i in range(N):
			n=int(input("Enter the number:"))
			data. append(n)
		print("Maximum:",max(data))
		print("Minimum:",min(data))
		print("Sum:",sum(data))
		print("Average:",sum(data)/len(data))
o=Calculate()#object Created
o.Numbers()#function call
