from math import ceil


def main():
    number_of_students = int(input())
    number_of_lectures = int(input())
    bonus = int(input())
    students = []
    if number_of_students == 0:
        print(f'Max Bonus: 0.\nThe student has attended 0 lectures.')
    else:

        for _ in range(number_of_students):
            student_attendance = int(input())
            students.append(student_attendance)

        student_with_max_attendances = max(students)
        total_bonus = student_with_max_attendances / number_of_lectures * (5 + bonus)
        print(f'Max Bonus: {ceil(total_bonus)}.\nThe student has attended {student_with_max_attendances} lectures.')


if __name__ == '__main__':
    main()

