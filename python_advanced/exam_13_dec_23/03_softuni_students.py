def softuni_students(*args, **kwargs):
    invalid_students = []
    valid_students = {}
    result = []
    for course_id, username in args:
        if course_id in kwargs:
            if username not in valid_students:
                valid_students[username] = []
            valid_students[username].append(kwargs[course_id])
        else:
            invalid_students.append(username)

    sorted_result = sorted(valid_students.items())

    [result.append(f'*** A student with the username {student} has successfully finished the course {course}!')
     for student, courses in sorted_result for course in courses]
    if invalid_students:
        result.append(f'!!! Invalid course students: {", ".join(sorted(invalid_students))}')

    return "\n".join(result)


print(softuni_students(
    ('id_22', 'Programmingkitten'),
    ('id_11', 'MitkoTheDark'),
    ('id_321', 'Bobosa253'),
    ('id_08', 'KrasimirAtanasov'),
    ('id_32', 'DaniBG'),
    id_321='HTML & CSS',
    id_22='Machine Learning',
    id_08='JS Advanced',
))
