command = input()

total_tickets = 0
movie_tickets = 0
student_tickets = 0
standard_tickets = 0
kid_tickets = 0
is_end = False

while command != 'Finish':
    free_spaces = int(input())

    while True:
        if free_spaces == movie_tickets:
            break

        ticket_type = input()

        if ticket_type == 'End':
            break

        movie_tickets += 1
        total_tickets += 1

        if ticket_type == 'standard':
            standard_tickets += 1

        elif ticket_type == 'student':
            student_tickets += 1

        elif ticket_type == 'kid':
            kid_tickets += 1

    print(f'{command} - {movie_tickets / free_spaces * 100:.2f}% full.')
    command = input()
    movie_tickets = 0

print(f'Total tickets: {total_tickets}')
print(f'{student_tickets / total_tickets * 100:.2f}% student tickets.')
print(f'{standard_tickets / total_tickets * 100:.2f}% standard tickets.')
print(f'{kid_tickets / total_tickets * 100:.2f}% kids tickets.')