from bankAccount import BankAccount


SergioAccount = BankAccount(0.05, 1000) #opening with initial deposit & special interest rate
PatriciaAccount = BankAccount() #opening a normal account without initial deposit

print("** Mov. Sergio's account **")
SergioAccount.deposit(4000)
SergioAccount.withdraw(500)
SergioAccount.deposit(1000)
SergioAccount.deposit(2000)
SergioAccount.yield_interest().display_account_info() #interes of 5% annual
print("** END **")

print("** Mov. Patricia's account **")
PatriciaAccount.withdraw(200) #charge $5 insufficient funds
PatriciaAccount.deposit(3000)
PatriciaAccount.withdraw(600)
PatriciaAccount.withdraw(7000) #charge $5 insufficiente funds
PatriciaAccount.deposit(5000)
PatriciaAccount.withdraw(4000)
PatriciaAccount.yield_interest().display_account_info() #interes of 1% annual
print("** END **")


print("*** BONUS ***")
#BONUS: Print all instances of a Bank Account's Info
BankAccount.printAllAccountInfo()
