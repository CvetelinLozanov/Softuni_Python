from basic_bank_account_system.bank_account import BankAccount
from basic_bank_account_system.client import Client
from basic_bank_account_system.savings_account import Savings
from basic_bank_account_system.test_bank import TestBank

if __name__ == '__main__':
    bank = TestBank()
    client = Client("Ivan", "Dimitrov", "Georgiev", "9611055414", '05.11.1996'
                    , 'street test')

    bank.create_user(client)
    bank.create_user(client)
    bank.create_user(client)
    print(bank.create_user(client))
    client1 = Client("Dragan", "Dimitrov", "Ivanov", "9611055413", '05.11.1996'
                    , 'street test')
    print(bank.deposit_money_in_bank_account(client1, 500))
    bank.create_saving_account(client, 1000)
    # bank.create_saving_account(client, 2000)
    # bank.create_saving_account(client, 3000)
    bank.print_user_saving_accounts_information(client)
    test = 1
    #bank.visualize_historical_interest_rate()
    # account = BankAccount(1000)
    # account.deposit(500)
    # account.withdraw(200)
    # #print(account.account_number)
    # account2 = BankAccount(100)
    # #print(account2.account_number)
    # print(account.get_balance())
    # savings = Savings(2000, 5)
    # savings.deposit(1000)
    # savings.calculate_interest()
    # print(savings.get_balance())


