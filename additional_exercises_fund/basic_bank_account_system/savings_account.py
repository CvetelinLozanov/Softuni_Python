from basic_bank_account_system.bank_account import BankAccount
from basic_bank_account_system.client import Client


class Savings(BankAccount):
    __account_number = 1

    def __init__(self, client: Client, balance: float, interest_rate: float=0):
        super().__init__(client, balance)
        self.interest_rate = interest_rate
        self.account_number = Savings.__account_number
        Savings.__account_number += 1

    def calculate_interest(self):
        self._balance *= 1 + (self.interest_rate / 100)
        return f"Your saving balance for account: {self.account_number} is {self._balance}"
