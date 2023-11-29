movie = input()
days = int(input())
tickets = int(input())
price_for_ticket = float(input())
percentage = int(input()) / 100

total_price_for_tickets = tickets * price_for_ticket
total_price = total_price_for_tickets * days
studio_bonus = total_price * percentage
total_price -= studio_bonus

print(f'The profit from the movie {movie} is {total_price:.2f} lv.')
