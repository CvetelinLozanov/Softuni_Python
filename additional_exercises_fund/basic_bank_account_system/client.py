from typing import List
from basic_bank_account_system.bank_account import BankAccount


class Client:
    def __init__(self, first_name: str, surname: str, last_name: str, EGN: str, date_of_birth: str):
        self.first_name = first_name,
        self.surname = surname
        self.last_name = last_name
        self.EGN = EGN
        self.date_of_birth = date_of_birth
        self.bank_account: List[BankAccount] = []