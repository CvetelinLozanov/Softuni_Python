deposit = float(input())
deadline_for_deposit = int(input())
yearly_percentage = float(input()) / 100
cash_to_receive = deposit + deadline_for_deposit * ((deposit * yearly_percentage) / 12)
print(cash_to_receive)