import os
import django
from datetime import date

# Set up Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "orm_skeleton.settings")
django.setup()

# Import your models here
from main_app.models import Student

"""
FC5204 John Doe 15/05/1995 john.doe@university.com
FE0054 Jane Smith null jane.smith@university.com
FH2014 Alice Johnson 10/02/1998 alice.johnson@university.com
FH2015 Bob Wilson 25/11/1996 bob.wilson@university.com
"""


def add_students():
    students_info = ['FC5204 John Doe 1995-05-15 john.doe@university.com',
                     'FE0054 Jane Smith null jane.smith@university.com',
                     'FH2014 Alice Johnson 1998-02-10 alice.johnson@university.com',
                     'FH2015 Bob Wilson 1996-11-25 bob.wilson@university.com']
    students = []

    for s in students_info:
        student_id, first_name, last_name, birth_date, email = s.split()
        students.append(Student(
            student_id=student_id,
            first_name=first_name,
            last_name=last_name,
            birth_date=None if birth_date == 'null' else birth_date,
            email=email
        ))

    Student.objects.bulk_create(students)


def get_students_info():
    result = []
    for s in Student.objects.all():
        result.append(f"Student №{s.student_id}: {s.first_name} {s.last_name}; Email: {s.email}")

    return '\n'.join(result)


def update_students_emails():
    all_students = Student.objects.all()
    for s in all_students:
        s.email = s.email.replace(s.email.split('@')[1], 'uni-students.com')

    Student.objects.bulk_update(all_students, ['email'])


def truncate_students():
    Student.objects.all().delete()

# Run and print your queries