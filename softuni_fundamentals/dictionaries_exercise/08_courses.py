from typing import Dict, List



def register_students(courses: Dict, course_name: str, student: str):
    if course_name not in courses:
        courses[course_name] = []

    courses[course_name].append(student)
    return courses


def print_courses(courses: Dict[str, List[str]]):
    for course, students in courses.items():
        print(f'{course}: {len(students)}')

        for student in students:
            print(f'-- {student}')


courses = {}

while True:
    command = input()

    if command == 'end':
        break

    course_name, student = command.split(' : ')
    courses = register_students(courses, course_name, student)

print_courses(courses)
