# Assignment 8.1
# This week we will work with classes by creating a banking program.  
# Your program should will use the inheritance diagram from this week 
# in order to create a parent class and two child classes.  Your program 
# will create an object of each type (CheckingAccount and SavingsAccount).
# Your program will use the following data:
# Balance: $100, $25
# Fees: $5
# Minimum Balance $50
# Interest Rate: 2%
# You will need to run the program twice.  Once with the account balance of 
# $100 and once with the account balance of $25. Since the second run of the 
# program will have a balance lower than the minimum balance a message should 
# be output letting the user know that their account is below the minimum balance.  
# Incorporate the good coding practices you have learned up to this point in the 
# course such as Try/Except Blocks, allow the user to continue to run the program 
# and to exit the program, formatting methods, etc.

def Main():

	# Parent Class
	class BankAccount():
		def __init__(self, accountNumber, balance):
		# initializing account number and balance attributes
			self.accountNumber = accountNumber
			self.balance = balance

		# withdrawal function 
		def withdrawal(self):
			amt_withdraw = float(input("How much do you want to withdraw: "))
			# compare the amt_withdraw to the balance
			if amt_withdraw <= self.balance:
				self.balance = self.balance - amt_withdraw
			else:
				# error message
				print("Invalid amount. Your balance is $"+str(self.balance)+ ".")
			return self.balance

		# Deposit function
		def deposit(self):
			amt_deposit = float(input("How much do you want to deposit: "))
			self.balance = self.balance + amt_deposit
			print("Your new balance is $"+str(self.balance)+".")
			return self.balance

		def getBalance(self):
			return self.balance


	# Child Classes
	class CheckingAccount(BankAccount):
		# class variables
		minimumBalance = 50
		fees = 5

		def __init__(self, accountNumber, balance):
			super().__init__(accountNumber, balance)

		def deductFees(self):
			self.balance = balance - fees
			return self.balance

		def checkMinimumBalance(self):
			if self.balance < minimumBalance:
				print("Your account is below the minimum balance of $"+ str(minimumBalance)+ ".")
				print("A $"+str(fees)+ " will be deducted from your account.")
				deductFees()


	class SavingsAccount(BankAccount):

		def __init__(self, accountNumber, balance, interestRate):
			super().__init__(accountNumber, balance)
			self.interestRate = interestRate

			def addInterest(self):
				interestAmt = self.balance * interestRate
				self.balance = self.balance + interestAmt
				return self.balance


	# 1st account information
	account_1 = BankAccount('1234', 100)


	# 2nd account information
	account_2 = BankAccount('5678', 25)



	print("Welcome to the BANK")
	userInput = input("Enter in your account number or enter quit: ")
	while userInput != 'quit':
		# Account_1
		if userInput == '1234':
			action = input("Do you want to:\n1. Check Account Balance\n2. Withdraw\n3. Make a Deposit")
			
			if action == '1':
				account_1.getBalance()
				print("Your account balance is $"+ str(account_1.balance)+ ".")
				userInput = input("Enter in your account number or enter quit: ")
			
			if action == '2':
				account_1.withdrawal()
				print("Your new balance is $"+ str(account_1.balance) + ".")
				account_1.checkMinimumBalance()
				userInput = input("Enter in your account number or enter quit: ")
			
			if action == '3':
				account_1.deposit()
				account_1 = SavingsAccount('1234', 100, 0.02)
				account_1.addInterest()
				print("Your new balance is $"+ str(account_1.balance) + ".")
				account_1.checkMinimumBalance()
				userInput = input("Enter in your account number or enter quit: ")

		# Account_2
		if userInput == '5678':
			action = input("Do you want to:\n1. Check Account Balance\n2. Withdraw\n3. Make a Deposit")
			
			if action == '1':
				account_2.getBalance()
				print("Your account balance is $"+ str(account_2.balance)+ ".")
				userInput = input("Enter in your account number or enter quit: ")
			
			if action == '2':
				account_2.withdrawal()
				print("Your new balance is $"+ str(account_2.balance) + ".")
				account_2.checkMinimumBalance()
				userInput = input("Enter in your account number or enter quit: ")
			
			if action == '3':
				account_2.deposit()
				account_2 = SavingsAccount('5678', 25, 0.02)
				account_2.addInterest()
				print("Your new balance is $"+ str(account_2.balance) + ".")
				account_2.checkMinimumBalance()
				userInput = input("Enter in your account number or enter quit: ")
		
		else:
			print("Invalid account number.")
			userInput = input("Enter in your account number or enter quit: ")

Main()