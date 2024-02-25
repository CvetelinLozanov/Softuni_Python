from basic_bank_account_system.bank_account import BankAccount


class Savings(BankAccount):
    __account_number = 1

    def __init__(self, balance: float, interest_rate=0):
        super().__init__(balance)
        self.interest_rate = interest_rate
        self.account_number = Savings.__account_number
        Savings.__account_number += 1

    def calculate_interest(self):
        self.balance *= 1 + (self.interest_rate / 100)
        return f"Your saving balance is {self.balance}"
