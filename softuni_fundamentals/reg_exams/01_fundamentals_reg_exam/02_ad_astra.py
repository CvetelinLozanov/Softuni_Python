import re


text = input()
pattern = r'([#|])([a-zA-Z\s]+)\1([0-9]{2}([\/])[0-9]{2}\4[0-9]{2})\1([0-9]|[1-9][0-9]|[1-9][0-9][0-9]|[1-9][0-9][0-9][0-9]|10000)\1'
matches = re.findall(pattern, text)
total_calories = 0

for match in matches:
    total_calories += int(match[4])

days = int(total_calories / 2000)

print(f'You have food to last you for: {days} days!')

for match in matches:
    print(f'Item: {match[1]}, Best before: {match[2]}, Nutrition: {match[4]}')