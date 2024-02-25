from typing import List
from basic_bank_account_system.bank_account import BankAccount
from basic_bank_account_system.client import Client
from abc import ABC, abstractmethod


class Bank(ABC):
    def __init__(self, name: str):
        self.name = name
        self.__clients: List[Client] = []
        self.__bank_accounts: List[BankAccount] = []

    @abstractmethod
    def create_user(self, user: Client):
        pass