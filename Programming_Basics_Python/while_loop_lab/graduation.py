name_of_student = input()
number_of_classes = 0
failed_classes = 0
grades_sum = 0

while number_of_classes < 12:
    grade = float(input())

    if grade < 4:
        failed_classes += 1

        if failed_classes > 1:
            number_of_classes += 1
            print(f'{name_of_student} has been excluded at {number_of_classes} grade')
            break

        continue

    number_of_classes += 1
    grades_sum += grade
else:
    print(f'{name_of_student} graduated. Average grade: {grades_sum / number_of_classes:.2f}')
