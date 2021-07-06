class BankAccount:
    all_accounts_list = []
    def __init__(self, account_name=None, int_rate=None, balance=None):
        if account_name is None:
            account_name = "Checking"
        self.account_name = account_name
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
        print("Balance: $"+str(self.balance))
        return self
    def yield_interest(self):
        self.balance += (self.balance * self.int_rate)
        return self
    @classmethod
    def all_accounts(cls):
        for account in cls.all_accounts_list:
            print("Rate: ",account.int_rate, ",Balance: $", account.balance)
# USER            
class User:		# here's what we have so far
    def __init__(self, name, email, account):
        self.name = name
        self.email = email
        self.all_accounts = []
        self.all_accounts.append(account)
    def user_deposit(self, account, amount):
        for accounts in self.all_accounts:
            if(accounts.account_name == account):
                accounts.deposit(amount)
        return self
    def user_withdrawal(self, account, amount):
        for accounts in self.all_accounts:
            if(accounts.account_name == account):
                accounts.withdraw(amount)
        return self
    def add_account(self, account):
        self.all_accounts.append(account)
        return self
    def display_user_details(self):
        firstString = self.name + " has " + str(len(self.all_accounts)) + " account(s)"
        print(firstString)
        for i in range(0, len(self.all_accounts), 1):
            print(self.all_accounts[i].account_name + " : $" + str(self.all_accounts[i].balance) + " available, interest of " + str(self.all_accounts[i].int_rate))
        return self
testUser = User('John Doe', 'user.name@gmail.com', BankAccount('Checking', .02, 100))
testUser.display_user_details()