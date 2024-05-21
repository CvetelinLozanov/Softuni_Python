from project.waiters.base_waiter import BaseWaiter


class FullTimeWaiter(BaseWaiter):
    def __init__(self, name: str, hours_worked: int):
        super().__init__(name, hours_worked)

    def calculate_earnings(self):
        self.total_earnings = self.hours_worked * 15
        return self.hours_worked * 15

    def report_shifts(self):
        return f"{self.name} worked a full-time shift of {self.hours_worked} hours."
