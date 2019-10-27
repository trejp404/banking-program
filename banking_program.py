# Prepedigna Trejo
# Assignment 8.1

# Parent Class - Account
class BankAccount:

	def __init__(self, num, bal):
		self.accountNumber = num
		self.balance = float(bal)
		print("A Pre-Paid Account has been created")
		print("The account number is " + str(self.accountNumber))
		print("The balance is $" + '{:,.2f}'.format(self.balance))

	def withdraw(self):
		userWithdraw = float(input("How much would you like to withdraw? "))
		if self.balance >= userWithdraw:
			self.balance = self.balance - float(userWithdraw)
			print ("\nYou Withdrew:", '$'+'{:,.2f}'.format(userWithdraw))
			self.getBalance()
		else:
			print("\nInsufficient funds")
			print("Your current account balance is:", '{:,.2f}'.format(self.balance))

	def deposit (self):
		userDeposit = input("How much would you like to deposit? ")
		self.balance = self.balance + float(userDeposit)
		self.getBalance()

	def getBalance(self):
		print("Current account balance is: $" + '{:,.2f}'.format(self.balance))

# child class 1 - Pre-Paid Account
class CheckingAccount(BankAccount):

	def __init__(self, num, bal, accountFees, minBal):
		BankAccount.__init__(self, num, bal)
		self.accountFees = accountFees
		self.minimumBalance = 50
		print("This account is a Checking Account")
		print("The account fee is $" + '{:,.2f}'.format(self.accountFees))
		print("The minimum balance is $" + '{:,.2f}'.format(self.minimumBalance))


	def deductFees(self):
		print("Deducting fee...")
		if self.balance < self.minimumBalance:
			self.balance -= 5;
		else:
			print("Balance after fee is now $" + '{:,.2f}'.format(self.balance))

	def checkMinimumBalance(self):
		print("Checking if account balance meets minimum balance...")
		print("")

		if float(self.balance) < self.minimumBalance:
			print("Account balance is too low")
			self.deductFees()
			print("You must deposit $" + '{:,.2f}'.format(self.minimumBalance - self.balance) + " to meet the minimum account balance")
			self.deposit()
			self.checkMinimumBalance()
		else:
			print("Account balance meets minimum balance requirements")

#child class 2 - Savings Account
class SavingsAccount(BankAccount):

	def __init__(self, num, bal, intRate):
		self.intRate = 2
		super().__init__(num, bal)

	def add_interest(self):
		self.balance *= (1 + (self.intRate/100))

# main program
print ("Welcome to the Program")

try:
	flag1 = 0
	while flag1 == 0:
		print("")
		print("--Main Menu--")
		print("To open a pre-paid account, press 1")
		print("To exit the program, press 2")
		loop1 = input("")

		if loop1 == '1':
			flag2 = 0
			while flag2 == 0:
				flag2 = 1
				print("")
				print("--Account Creation--")
				print("To open a Checking Account, press 1")
				loop2 = input("")

				if loop2 == '1':
					print("")
					print("--Open a Checking Account--")
					print("Minimum Balance is $50.00")
					print("Account fees are $5.00")
					checkingAccountNumber = input("Enter an Account Number: ")
					checkingAccountBalance = input("Enter Account Balance: $")
					print("Please wait while account is created...")
					print("")
					my_checkingAccount = CheckingAccount(checkingAccountNumber, checkingAccountBalance, 5.0, 50.0)
					my_checkingAccount.checkMinimumBalance()

					flag3 = 0
					while flag3 == 0:
						print("")
						print("--My Checking Account--")
						print("What would you like to do?")
						print("To make a deposit, press 1")
						print("To check your balance, press 3")
						print("To make a withdrawal, press 4")
						print("To go to the Main Menu, press 5")
						loop3 = input("")

						if loop3 == '1':
							my_checkingAccount.deposit()
						elif loop3 == '3':
							my_checkingAccount.getBalance()
						elif loop3 == '4':
							my_checkingAccount.withdraw()
						elif loop3 == '5':
							print("Exiting to Main Menu...")
							flag3 = 1
						else:
							print("Command not recognized")

				else:
					print("Command not recognized")
					flag2 = 0
		elif loop1 == '2':
			print("Exiting program...")
			flag1 = 1
		else:
			print("Command not recognized")
except:
	print("Command not recognized")