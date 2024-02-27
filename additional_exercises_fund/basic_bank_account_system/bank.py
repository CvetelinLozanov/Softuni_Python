from typing import List
from basic_bank_account_system.bank_account import BankAccount
from basic_bank_account_system.client import Client
from abc import ABC, abstractmethod
from basic_bank_account_system.savings_account import Savings


class Bank(ABC):
    def __init__(self, name: str):
        self.name = name
        self._clients: List[Client] = []
        self._bank_accounts: List[BankAccount] = []
        self._saving_accounts:List[Savings] = []

    @abstractmethod
    def create_user(self, user: Client):
        pass

    @abstractmethod
    def deposit_money_in_bank_account(self, client: Client, balance: float):
        pass

    def create_saving_account(self, user: Client, balance: float):
        pass