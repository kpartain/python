class BankAccount:
    all_accounts_list = []
    def __init__(self, int_rate=None, balance=None): 
        if int_rate is None:
            int_rate = 0.01
        self.int_rate = int_rate
        if balance is None:
            balance = 0
        self.balance = balance
        BankAccount.all_accounts_list.append(self)
    def deposit(self, amount):
        # your code here
        self.balance += amount
        return self
    def withdraw(self, amount):
        # your code here
        self.balance -= amount
        if(self.balance < 0):
            self.balance -= 5
            print("Insufficient funds: Charging a $5 fee")
            
        return self
    def display_account_info(self):
        # your code here
        print("Balance: $"+str(self.balance))
        return self
    def yield_interest(self):
        # your code here
        self.balance += (self.balance * self.int_rate)
        return self
    @classmethod
    def all_accounts(cls):
        for account in cls.all_accounts_list:
            print("Rate: ",account.int_rate, ",Balance: $", account.balance)
testAccount = BankAccount(.02, 200).deposit(100).withdraw(105).deposit(200).yield_interest()
print("New account")
testAccount2 = BankAccount().deposit(100).withdraw(105).deposit(200).yield_interest()

BankAccount.all_accounts()