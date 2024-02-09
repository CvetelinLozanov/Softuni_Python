def are_employees_happy():
    employees = list(map(int, input().split()))
    happiness_factor = int(input())
    employees_happiness = [emp * happiness_factor for emp in employees]
    average_happiness = sum(employees_happiness) / len(employees)
    happy_employees = list(filter(lambda x: x >= average_happiness, employees_happiness))
    happy_or_not = 'happy' if len(happy_employees) >= len(employees) / 2 else 'not happy'

    return f'Score: {len(happy_employees)}/{len(employees)}. Employees are {happy_or_not}!'


print(are_employees_happy())
