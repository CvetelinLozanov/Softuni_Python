from basic_bank_account_system.bank_account import BankAccount
from basic_bank_account_system.savings_account import Savings

if __name__ == '__main__':
    account = BankAccount(1000)
    account.deposit(500)
    account.withdraw(200)
    print(account.account_number)
    account2 = BankAccount(100)
    print(account2.account_number)
    print(account.get_balance())
    savings = Savings(2000, 5)
    savings.deposit(1000)
    savings.calculate_interest()
    print(savings.balance)


