from typing import List

from project.clients.base_client import BaseClient
from project.clients.adult import Adult
from project.clients.student import Student
from project.loans.base_loan import BaseLoan
from project.loans.student_loan import StudentLoan
from project.loans.mortgage_loan import MortgageLoan


class BankApp:
    LOANS = {'StudentLoan': StudentLoan, "MortgageLoan": MortgageLoan}
    CLIENTS = {"Student": Student, "Adult": Adult}

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.loans: List[BaseLoan] = []
        self.clients: List[BaseClient] = []

    def add_loan(self, loan_type: str):
        if loan_type not in self.LOANS:
            raise Exception("Invalid loan type!")

        self.loans.append(self.LOANS[loan_type]())
        return f"{loan_type} was successfully added."

    def add_client(self, client_type: str, client_name: str, client_id: str, income: float):
        if client_type not in self.CLIENTS:
            raise Exception("Invalid client type!")

        if len(self.clients) >= self.capacity:
            return "Not enough bank capacity."

        self.clients.append(self.CLIENTS[client_type](client_name, client_id, income))
        return f"{client_type} was successfully added."

    def grant_loan(self, loan_type: str, client_id: str):
        client = self._get_client(client_id)
        if client.__class__.__name__ == 'Student' and loan_type != 'StudentLoan':
            raise Exception("Inappropriate loan type!Inappropriate loan type!")

        if client.__class__.__name__ == 'Adult' and loan_type != 'MortgageLoan':
            raise Exception("Inappropriate loan type!Inappropriate loan type!")

        loan = self._get_first_loan(loan_type)
        client.loans.append(loan)
        self.loans.remove(loan)
        return f"Successfully granted {loan_type} to {client.name} with ID {client_id}."

    def remove_client(self, client_id: str):
        client = self._get_client(client_id)
        if not client:
            raise Exception("No such client!")

        if client.loans:
            raise Exception("The client has loans! Removal is impossible!")

        self.clients.remove(client)
        return f"Successfully removed {client.name} with ID {client_id}."

    def increase_loan_interest(self, loan_type: str):
        counter = 0

        for loan in self.loans:
            if loan.__class__.__name__ == loan_type:
                loan.increase_interest_rate()
                counter += 1

        return f"Successfully changed {counter} loans."

    def increase_clients_interest(self, min_rate: float):
        counter = 0

        for client in self.clients:
            if client.interest < min_rate:
                client.increase_clients_interest()
                counter += 1

        return f"Number of clients affected: {counter}."

    def get_statistics(self):
        total_clients = len(self.clients)
        total_clients_income = sum([client.income for client in self.clients])
        granted_loans_sum = sum([loan.amount for client in self.clients for loan in client.loans])
        granted_loans_count = sum([len(client.loans) for client in self.clients])
        not_granted_loans_sum = sum([loan.amount for loan in self.loans])
        not_granted_loans_count = len(self.loans)
        avg_interest_rate = 0 if len(self.clients) == 0 \
            else sum([client.interest for client in self.clients]) / len(self.clients)

        result = (f"Active Clients: {total_clients}\nTotal Income: {total_clients_income:.2f}\n"
                  f"Granted Loans: {granted_loans_count}, Total Sum: {granted_loans_sum:.2f}\n"
                  f"Available Loans: {not_granted_loans_count}, Total Sum: {not_granted_loans_sum:.2f}\n"
                  f"Average Client Interest Rate: {avg_interest_rate:.2f}")

        return result.strip()

    def _get_client(self, client_id: str):
        client = [client for client in self.clients if client.client_id == client_id]
        return client[0] if client else None

    def _get_first_loan(self, loan_type: str):
        loan = [loan for loan in self.loans if loan.__class__.__name__ == loan_type]
        return loan[0] if loan else None