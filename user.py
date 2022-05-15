from bank_account import Bnk_account

class User:

    def __init__(self, name, email, account):
        self.name = name
        self.email = email 
        self.account = account

    def deposit(self, amount):
        self.account.deposit(amount)
        
    def  make_withdraw(self, amount):
        self.account.make_withdraw(amount)
        
    def display_bal(self):
        print(f"{self.name}" * 1)
        self.account.display_bal
        
    def balance(self):
        self.account = self.balance()

    def make_transfer(self, other_user, amount):
        self.make_withdraw(amount)
        other_user.deposit(amount)

baccount1 = Bnk_account()
baccount2 = Bnk_account()

user1 = User("David", "david@dojo.com", "account1")
user2 = User("Skylar", "skylar@dojo.com", "account2")