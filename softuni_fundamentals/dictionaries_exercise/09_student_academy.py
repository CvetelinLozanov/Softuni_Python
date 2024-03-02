from typing import List, Dict


def filter_students_with_higher_grades(students: Dict[str, List[float]]):
    return {student: f'{sum(grades) / len(grades):.2f}' for student, grades in students.items()
            if sum(grades) / len(grades) >= 4.50}
    # filter_students = {}
    # for student, grades in students.items():
    #     if sum(grades) / len(grades) >= 4.50:
    #         filter_students[student] = f'{sum(grades)} / {len(grades):.2f}'
    #
    # return filter_students


def print_students(students_with_higher_grades: Dict[str, List[str]]):
    [print(f'{student} -> {avg_grade}') for student, avg_grade in students_with_higher_grades.items()]


n = int(input())
students = {}

for _ in range(n):
    student = input()
    grade = float(input())

    if student not in students:
        students[student] = []

    students[student].append(grade)

students_with_higher_grades = filter_students_with_higher_grades(students)
print_students(students_with_higher_grades)