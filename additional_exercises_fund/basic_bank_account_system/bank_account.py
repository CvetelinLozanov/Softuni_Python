class BankAccount:
    MAX_MONEY_TO_WITHDRAW_PER_DAY = 2000
    __account_number = 1

    def __init__(self, balance: float):
        self.balance = balance
        self.account_number = BankAccount.__account_number
        BankAccount.__account_number += 1

    def deposit(self, amount: float):
        self.balance += amount

    def withdraw(self, amount: float):
        if amount > self.balance:
            return f"You've entered too big amount to withdraw. Your balance is {self.get_balance()}"

        if amount > self.MAX_MONEY_TO_WITHDRAW_PER_DAY:
            return "You can withdraw maximum 2000$ per day"

        self.balance -= amount
        return f"You have successfully withdraw {amount} from your account"

    def get_balance(self):
        return self.balance
