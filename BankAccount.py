
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
            print("Your new balance is $"+ str(self.balance) + ".")
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
        print("Your balance is $"+str(self.balance)+".")


# Child Classes #1
class CheckingAccount(BankAccount):

    def __init__(self, accountNumber, balance):
        super().__init__(accountNumber, balance)

    def deductFees(self):
        fees = 5
        self.balance -= fees
        print("There is a $"+str(fees)+" fee being charge to your account.")
        print("Your new balance is $"+ str(self.balance) + ".")
        return self.balance

    def checkMinimumBalance(self):
        minimumBalance = 50
        if self.balance < minimumBalance:
            print("Your account is below the minimum balance of $"+ str(minimumBalance)+ ".")
            self.deductFees()
        else:
            print("You are above the minimum balance of $"+str(minimumBalance)+".")

print("Welcome to the BANK\n")

# 1st account information and runthrough
account_1 = BankAccount(1234, 100)
account_1 = CheckingAccount(1234, 100)
print("Checking Account Number: " + str(account_1.accountNumber))
account_1.withdrawal()
account_1.deposit()
account_1.getBalance()
account_1.checkMinimumBalance()
print("\n")

# 2nd account information
account_2 = BankAccount(5678, 25)
account_2 = CheckingAccount(5678, 25)
print("Checking Account Number: " + str(account_2.accountNumber))
account_2.withdrawal()
account_2.deposit()
account_2.getBalance()
account_2.checkMinimumBalance()
print("\n")


class SavingsAccount(BankAccount):

    def __init__(self, accountNumber, balance, interestRate):
        super().__init__(accountNumber, balance)
        self.interestRate = interestRate

    def addInterest(self):
        self.balance = self.balance + (self.balance * self.interestRate)
        print("An interest rate of "+str(self.interestRate)+"% has been applied to your account.")
        print("Your new balance is $"+str(self.balance)+".")
        return self.balance


# 1st account information
account_1 = SavingsAccount(1234, 100, .02)
print("Savings Account Number: " + str(account_1.accountNumber))
account_1.withdrawal()
account_1.deposit()
account_1.getBalance()
print("Your interest rate is " +str(account_1.interestRate)+ "%.")
account_1.interestRate = 1.05
account_1.addInterest()
print("\n")


# 2nd account information
account_2 = SavingsAccount(5678, 25, .02)
print("Savings Account Number: " + str(account_2.accountNumber))
account_2.withdrawal()
account_2.deposit()
account_2.getBalance()
print("Your interest rate is " +str(account_1.interestRate)+ "%.")
account_1.interestRate = 1.08
account_2.addInterest()
print("\n")


