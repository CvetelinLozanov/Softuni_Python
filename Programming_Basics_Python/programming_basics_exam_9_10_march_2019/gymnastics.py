country = input()
device = input()

points_sum = 0

if country == 'Bulgaria':
    if device == 'ribbon':
        points_sum = 9.6 + 9.4
    elif device == 'hoop':
        points_sum = 9.55 + 9.75
    elif device == 'rope':
        points_sum = 9.5 + 9.4
elif country == 'Russia':
    if device == 'ribbon':
        points_sum = 9.1 + 9.4
    elif device == 'hoop':
        points_sum = 9.3 + 9.8
    elif device == 'rope':
        points_sum = 9.6 + 9
elif country == 'Italy':
    if device == 'ribbon':
        points_sum = 9.2 + 9.5
    elif device == 'hoop':
        points_sum = 9.45 + 9.35
    elif device == 'rope':
        points_sum = 9.7 + 9.15

percentage = 100 - (points_sum / 20 * 100)

print(f'The team of {country} get {points_sum:.3f} on {device}.')
print(f'{percentage:.2f}%')
