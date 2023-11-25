number_of_bad_grades = int(input())

grades_sum = 0
number_of_grades = 0
failed_grades = 0
last_problem = ''
name_of_exercise = input()

while name_of_exercise != 'Enough':

    grade = float(input())
    last_problem = name_of_exercise
    number_of_grades += 1
    grades_sum += grade
    if grade <= 4:
        failed_grades += 1
        if failed_grades >= number_of_bad_grades:
            print(f'You need a break, {number_of_bad_grades} poor grades.')
            break

    name_of_exercise = input()
else:
    print(f'Average score: {grades_sum / number_of_grades:.2f}')
    print(f'Number of problems: {number_of_grades}')
    print(f'Last problem: {last_problem}')
