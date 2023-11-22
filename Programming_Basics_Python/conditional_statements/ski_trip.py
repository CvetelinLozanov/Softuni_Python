days_for_rest = int(input())
type_of_room = input()
raiting = input()

number_of_nights = days_for_rest - 1
final_price_to_pay = 0

if type_of_room == 'room for one person':
    final_price_to_pay = number_of_nights * 18
elif type_of_room == 'apartment':
    final_price_to_pay = number_of_nights * 25
    if 0 < number_of_nights < 10:
        final_price_to_pay *= 0.70
    elif 10 <= number_of_nights <= 15:
        final_price_to_pay *= 0.65
    elif number_of_nights > 15:
        final_price_to_pay *= 0.5
elif type_of_room == 'president apartment':
    final_price_to_pay = number_of_nights * 35
    if 0 < number_of_nights < 10:
        final_price_to_pay *= 0.90
    elif 10 <= number_of_nights <= 15:
        final_price_to_pay *= 0.85
    elif number_of_nights > 15:
        final_price_to_pay *= 0.8

if raiting == 'positive':
    final_price_to_pay *= 1.25
elif raiting == 'negative':
    final_price_to_pay *= 0.90

print(f'{final_price_to_pay:.2f}')
