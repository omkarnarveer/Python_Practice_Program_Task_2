'''WAP to determine if the seller has made profit or loss.Display amount of profit/loss.(Input: Cost price and selling price).'''
class Seller:
	def amount(self):
		cp=float(input("Enter Cost Price: $"))
		sp=float(input("Enter Sekking Price: $"))
		pl=sp-cp
		if sp>cp:
			print("Profit made by seller is of amount: $",pl)
		elif cp>sp:
			print("Loss made by seller is of amount: $",pl)
		elif cp==sp:
			print("No Profit No Loss made by seller is of amount: $",pl)
s=Seller()
s.amount()
