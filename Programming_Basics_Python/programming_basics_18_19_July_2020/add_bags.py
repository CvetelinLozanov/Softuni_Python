price_for_luggage_20_kg = float(input())
kilograms_per_luggage = float(input())
days_till_trip = int(input())
number_of_luggage = int(input())

price_for_luggage = 0

if kilograms_per_luggage < 10:
    price_for_luggage = price_for_luggage_20_kg * 0.2

elif 10 <= kilograms_per_luggage <= 20:
    price_for_luggage = price_for_luggage_20_kg / 2

elif kilograms_per_luggage > 20:
    price_for_luggage = price_for_luggage_20_kg

if days_till_trip > 30:
    price_for_luggage *= 1.10

elif 7 <= days_till_trip <= 30:
    price_for_luggage *= 1.15

elif days_till_trip < 7:
    price_for_luggage *= 1.40

total_taxes = price_for_luggage * number_of_luggage

print(f'The total price of bags is: {total_taxes:.2f} lv.')