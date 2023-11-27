text = input()

student_counter = 0
kid_counter = 0
standard_counter = 0
total_tickets = 0
movie_ticket_counter = 0

while text != 'Finish':
    free_seats = int(input())
    type_of_ticket = input()

    while type_of_ticket != 'End':
        total_tickets += 1
        movie_ticket_counter += 1

        if type_of_ticket == 'student':
            student_counter += 1

        elif type_of_ticket == 'standard':
            standard_counter += 1

        elif type_of_ticket == 'kid':
            kid_counter += 1

        if movie_ticket_counter == free_seats:
            break

        type_of_ticket = input()

    print(f'{text} - {movie_ticket_counter / free_seats * 100:.2f}% full.')
    movie_ticket_counter = 0

    text = input()

else:
    print(f'Total tickets: {total_tickets}')
    print(f'{student_counter / total_tickets * 100:.2f}% student tickets.')
    print(f'{standard_counter / total_tickets * 100:.2f}% standard tickets.')
    print(f'{kid_counter / total_tickets * 100:.2f}% kids tickets.')
