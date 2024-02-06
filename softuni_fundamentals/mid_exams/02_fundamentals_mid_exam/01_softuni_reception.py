def calculate_total_time(_first_employee: int, _second_employee: int, _third_employee: int):
    return _first_employee + _second_employee + _third_employee


def calculate_time_needed(students_count: int):
    time_needed = 0
    while students_count > 0:
        students_count -= total_answers
        time_needed += 1
        if time_needed % 4 == 0:
            time_needed += 1

    return time_needed


first_employee, second_employee, third_employee = int(input()), int(input()), int(input())
students_count = int(input())
total_answers = calculate_total_time(first_employee, second_employee, third_employee)
time = calculate_time_needed(students_count)
print(f'Time needed: {time}h.')