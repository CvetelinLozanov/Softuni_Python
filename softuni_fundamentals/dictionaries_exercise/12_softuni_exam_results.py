def process_student_submissions(submissions, students, username, language, points):
    if username not in students:
        students[username] = []

    students[username].append(points)

    if language not in submissions:
        submissions[language] = 0

    submissions[language] += 1


def print_student_results(students):
    print('Results:')
    for student, submissions in students.items():
        print(f'{student} | {max(submissions)}')


def print_submissions(submissions):
    print('Submissions:')
    for language, num_of_submissions in submissions.items():
        print(f'{language} - {num_of_submissions}')


submissions = {}
banned_users = []
students = {}

while True:
    command = input()

    if command == 'exam finished':
        break

    command_args = command.split('-')

    if len(command_args) == 3:
        username, language, points = command_args
        points = int(points)
        process_student_submissions(submissions, students, username, language, points)

    elif len(command_args) == 2:
        username = command_args[0]
        if username in students:
            banned_users.append(username)
            del students[username]

print_student_results(students)
print_submissions(submissions)