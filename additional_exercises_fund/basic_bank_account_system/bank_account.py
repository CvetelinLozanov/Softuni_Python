from basic_bank_account_system.client import Client


class BankAccount:
    MAX_MONEY_TO_WITHDRAW_PER_DAY = 2000
    __account_number = 1

    def __init__(self, client: Client, balance: float):
        self._balance = balance
        self.client = client
        self.account_number = BankAccount.__account_number
        BankAccount.__account_number += 1

    def deposit(self, amount: float):
        self._balance += amount

    def withdraw(self, amount: float):
        if amount > self._balance:
            return f"You've entered too big amount to withdraw. Your balance is {self.get_balance()}"

        if amount > self.MAX_MONEY_TO_WITHDRAW_PER_DAY:
            return "You can withdraw maximum 2000$ per day"

        self._balance -= amount
        return f"You have successfully withdraw {amount} from your account"

    def get_balance(self):
        return self._balance
