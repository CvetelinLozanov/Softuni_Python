people_in_the_jury = int(input())
average_grade_for_student = 0
average_grade_for_all = 0
grade_counter = 0
all_grades_counter = 0
text = input()

while text != 'Finish':

    for grade in range(people_in_the_jury):
        input_grade = float(input())
        average_grade_for_student += input_grade
        average_grade_for_all += input_grade
        all_grades_counter += 1
        grade_counter += 1

    print(f'{text} - {average_grade_for_student / grade_counter:.2f}.')

    text = input()
    grade_counter = 0
    average_grade_for_student = 0


print(f'Student\'s final assessment is {average_grade_for_all / all_grades_counter:.2f}.')
