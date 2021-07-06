class User:		# here's what we have so far
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0
    # adding the deposit method
    def make_deposit(self, amount):	# takes an argument that is the amount of the deposit
    	self.account_balance += amount	# the specific user's account increases by the amount of the value received
    #make_withdrawal(self, amount) - have this method decrease the user's balance by the amount specified
    def make_withdrawal(self, amount):
        self.account_balance -= amount
        #not required to account for request above balance - no "overdraft" protection

    # display_user_balance(self) - have this method print the user's name and account balance to the terminal
    # eg. "User: Guido van Rossum, Balance: $150
    def display_user_balance(self):
        print("User:",self.name,", Balance: $"+str(self.account_balance))
    # BONUS: transfer_money(self, other_user, amount) - have this method decrease the user's balance by the amount and add that amount to other other_user's balance
    def transfer_money(self, other_user, amount):
        self.account_balance -= amount
        other_user.make_deposit(amount)
karaUser = User("Kara", "kara@email.com")
karaUser.make_deposit(500)
karaUser.make_withdrawal(200)
karaUser.display_user_balance()

testUser = User("Testman", "Test@Test.com")
testUser.make_deposit(100)
testUser.display_user_balance()

karaUser.transfer_money(testUser, 100)
karaUser.display_user_balance()
testUser.display_user_balance()