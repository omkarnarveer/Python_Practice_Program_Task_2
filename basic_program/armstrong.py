'''WAP to determine if the given number is the Armstrong number or not (153 is the Armstrong number as 1³+5³+3³=153).'''
class Armstrong:
	def Number(self):
		num= int(input("Enter Number:"))
		sum = 0
		temp = num
		while temp>0:
			digit = temp%10
			sum += digit ** 3
			temp//=10
		if num == sum:
			print(num,"is an Armstrong Number")
		else:
			print(num,"is not an Armstrong Number")
o=Armstrong()
o.Number()
