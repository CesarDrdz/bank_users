

class Bnk_account:

    bank_name = "Last Credit Union"
    all_Accounts = []

    def __init__(self, interest_rate=0.2, balance=0) -> None:
        self.interest_rate = interest_rate
        self.balance = balance

    def deposit(self, amount):
        self.account.make_deposit(amount)
        # self.balance += amount
        return self

    def make_withdraw(self, amount):
        self.balance -= amount
        return self 

    def display_bal(self):
        print(f"the current balance is: {self.balance}")
        return self

    def yield_interest(self):
        self.balance = self.balance * self.interest_rate + self.balance
        return self

account = Bnk_account