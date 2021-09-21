class BankAccount:

    allBankAccounts =[]
    def __init__(self, int_rate=0.01, balance=0.0):
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.allBankAccounts.append(self)

    def deposit(self, amount=0):
        self.balance += amount

    def withdraw(self, amount=0):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5

    def display_account_info(self):
        print(f"Balance: ${self.balance}.")
        return self

    def yield_interest(self):
        if self.balance > 0:
            interest = self.balance*self.int_rate
            self.balance += interest
        return self

    @classmethod
    def printAllAccountInfo(cls):
        for account in cls.allBankAccounts:  
            account.display_account_info()
