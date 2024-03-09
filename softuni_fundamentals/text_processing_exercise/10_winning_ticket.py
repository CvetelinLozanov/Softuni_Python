def check_ticket(ticket: str):
    valid_symbols = ['@', '#', '$', '^']
    left_part = ticket[:10]
    right_part = ticket[10:]
    if len(ticket) != 20:
        return 'invalid ticket'

    for symbol in valid_symbols:
        for uninterrupted_match_length in range(10, 5, -1):
            current_win_ticket = symbol * uninterrupted_match_length

            if current_win_ticket in left_part and current_win_ticket in right_part:
                if len(current_win_ticket) == 10:
                    return f'ticket "{ticket}" - {uninterrupted_match_length}{symbol} Jackpot!'

                return f'ticket "{ticket}" - {uninterrupted_match_length}{symbol}'

    return f'ticket "{ticket}" - no match'


tickets = [ticket.strip() for ticket in input().split(', ')]

for current_ticket in tickets:
    print(check_ticket(current_ticket))