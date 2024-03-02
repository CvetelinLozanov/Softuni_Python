companies = {}

while True:

    command = input()

    if command == 'End':
        break

    company, employee_id = command.split(' -> ')

    if company not in companies:
        companies[company] = []

    if employee_id not in companies[company]:
        companies[company].append(employee_id)

for company, employee_ids in companies.items():
    print(company)
    for employee in employee_ids:
        print(f'-- {employee}')