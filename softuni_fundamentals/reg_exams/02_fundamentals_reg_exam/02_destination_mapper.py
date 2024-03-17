import re

destinations = input()
pattern = r'([=\/])([A-Z][a-zA-Z]{2,})\1'
matches = re.findall(pattern, destinations)

travel_points = 0

for match in matches:
    travel_points += len(match[1])

print(f'Destinations: {", ".join([match[1] for match in matches])}')
print(f'Travel Points: {travel_points}')
