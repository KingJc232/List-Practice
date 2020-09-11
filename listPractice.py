

class Wasted:
	def __init__(self, month, amount):
		self._month = month
		self._amount = amount

	@property
	def month(self):
		return self._month
	
	@property
	def amount(self):
		return self._amount
	
	@amount.setter
	def amount(self, newAmount):
		self._amount = newAmount

	@month.setter
	def month(self, newMonth):
		self._month = newMonth

	def __repr__(self):
		return str(self.month) + ": " + str(self.amount)

def main():

	expenses = [Wasted("January", 2200), Wasted("February", 2350), Wasted("March", 2600)
				,Wasted("April", 2130), Wasted("May", 2190)]

	totalExpense = 0 

	for expense in expenses:
		if expense.month == "February":
			print("Amount Spent in February $%s" % str(expense.amount))

	for i in range(3):
		totalExpense += expenses[int(i % len(expenses))].amount

	print("Total Expenses $%d" % totalExpense)

	amount = 2000 

	for exepense in expenses:
		if expense.amount == amount:
			print("Spend %d, in %s month" % expense.amount, expense.month)

	#Adding June Month
	expenses.append(Wasted("June", 1980))

	for i in range(len(expenses)):
		if expenses[i].month == "April":
			expenses[i].amount -= 200 #Got a 200 dollar refund

	print("Final List: ")
	print(expenses)

if __name__ == "__main__":
	main()













