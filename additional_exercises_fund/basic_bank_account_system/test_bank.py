import requests
import pandas as pd
import matplotlib.pyplot as plt
from typing import List
from basic_bank_account_system.Exceptions.invalid_account_exception import InvalidAccountException
from basic_bank_account_system.bank import Bank
from basic_bank_account_system.client import Client
from basic_bank_account_system.bank_account import BankAccount
from basic_bank_account_system.savings_account import Savings
from basic_bank_account_system.Exceptions.max_bank_accounts_exception import MaxBankAccountExceptions


class TestBank(Bank):
    def __init__(self):
        super().__init__('Test Bank')

    # Method to check if user already exists
    def __check_if_user_exists(self, user: Client):
        cur_user = self.__get_user(user)

        if cur_user:
            return True
        return False

    # Method to check if there are already bank accounts linked to the user and returns them if exists
    def __get_user_bank_accounts(self, user: Client):
        return [ba for ba in self._bank_accounts if ba.client.EGN == user.EGN]

    # Method to get user saving accounts
    def __get_user_saving_accounts(self, user: Client):
        return [sa for sa in self._saving_accounts if sa.client.EGN == user.EGN]

    # Method to get user by EGN
    def __get_user(self, user):
        new_user_egn = user.EGN
        return [c for c in self._clients if c.EGN == new_user_egn]

    # Method to create new user with new bank account in bank
    def create_user(self, user: Client):
        user_bank_accounts = self.__get_user_bank_accounts(user)

        if not self.__check_if_user_exists(user):
            self._clients.append(user)

        if len(user_bank_accounts) == 3:
            return f'User can have maximum 3 bank accounts'
            # raise MaxBankAccountExceptions("User can have maximum 3 bank accounts")

        user_new_bank_account = BankAccount(user, 0)
        self._bank_accounts.append(user_new_bank_account)

    # Method to print accounts if there are more than one
    @staticmethod
    def __print_bank_accounts_menu(accounts_ids: List[int]):
        print("You have more than one bank accounts. Please choose account id in which you want to add money.")
        print(f"Account IDs: {' '.join(map(str, accounts_ids))}")

    # Method to validate and return the account number chosen by user
    def get_account(self, accounts_ids: List[int]):
        while True:
            self.__print_bank_accounts_menu(accounts_ids)
            try:
                account = int(input('Please enter account you want to deposit money:'))
                if account not in accounts_ids:
                    raise InvalidAccountException()
                return account
            except InvalidAccountException:
                print(f'Please enter a valid account!!!')

    # Method to deposit money in bank account
    def deposit_money_in_bank_account(self, user: Client, balance: float):

        if not self.__check_if_user_exists(user):
            return f"User with name {user.first_name} {user.surname} {user.last_name} doesn't exists in our bank!"

        client_bank_accounts = self.__get_user_bank_accounts(user)

        if len(client_bank_accounts) == 1:
            client_bank_accounts[0].deposit(balance)
            new_balance = client_bank_accounts[0].get_balance()
            return f"{balance}$ have been added to your bank account. Your new balance is {new_balance}$"

        accounts_ids = [ac.account_number for ac in client_bank_accounts]
        chosen_account_to_deposit = self.get_account(accounts_ids)

        for account in client_bank_accounts:
            if account.account_number == chosen_account_to_deposit:
                account.deposit(balance)
                new_balance = account.get_balance()
                return (f"{balance}$ have been added to your bank account."
                        f" Your new balance in account {account.account_number} is {new_balance}$")

    # Method to create new saving account
    def create_saving_account(self, user: Client, balance: float):

        if not self.__check_if_user_exists(user):
            return f"User with name {user.first_name} {user.surname} {user.last_name} doesn't exists in our bank!"

        current_interest_rate = self.__fetch_data_for_current_euro_interest_rate()
        user_new_saving_account = Savings(user, balance, current_interest_rate)
        self._saving_accounts.append(user_new_saving_account)

    # Method to print user saving accounts balance
    def print_user_saving_accounts_information(self, user: Client):

        if not self.__check_if_user_exists(user):
            return f"User with name {user.first_name} {user.surname} {user.last_name} doesn't exists in our bank!"

        user_saving_accounts = self.__get_user_saving_accounts(user)

        if user_saving_accounts:
            print(f"User with name: {user.first_name} {user.surname} {user.last_name} have {len(user_saving_accounts)} "
                  f"saving account{'' if len(user_saving_accounts) == 1 else 's'}:")
            for saving_account in user_saving_accounts:
                print(saving_account.calculate_interest())

    # Method to get the data for current euro interest rate
    @staticmethod
    def __fetch_data_for_current_euro_interest_rate():
        api_url = 'https://api.estr.dev/latest'
        response = requests.get(api_url)
        if response.status_code == requests.codes.ok:
            data = response.json()
            return data['value']
        else:
            print("Error fetching the data for current interest rate")
            return None

    # Method to get the data for historical interest rate with api estr
    @staticmethod
    def __fetch_data_for_historical_euro_interest_rate():
        api_url = 'https://api.estr.dev/historical'
        response = requests.get(api_url)
        if response.status_code == requests.codes.ok:
            data = response.json()
            return data
        else:
            print("Error fetching the data for current interest rate")
            return None

    # Method to ge the data only for the latest 30 changes in rate
    @staticmethod
    def __historical_interest_rate(json_data):
        df = pd.DataFrame(json_data)
        df.index = pd.to_datetime(df['date'])
        df = df.iloc[:30]  # takes the information for last 30 changes
        df['value'].astype(float)
        df.columns = ['year', 'interest_rate']
        return df

    # Method to visualize european central bank historical interest rate
    def visualize_historical_interest_rate(self):
        data = self.__fetch_data_for_historical_euro_interest_rate()
        df = self.__historical_interest_rate(data)
        plt.figure(figsize=(10, 6), facecolor='white')
        plt.plot(df.index, df['interest_rate'], color='blue', label='Percentage')
        plt.title(f'Historical Interest rate')
        plt.xlabel('Interest Rate')
        plt.grid(True)
        plt.legend(loc="upper left")
        plt.show()
