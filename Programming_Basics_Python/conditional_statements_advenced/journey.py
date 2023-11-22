budget = float(input())
season = input()
is_hotel = False
is_camp = False
location = ''
costs = 0

if 0 < budget <= 100:
    location = 'Bulgaria'
    if season == 'summer':
        costs = budget * 0.3
        is_camp = True
    elif season == 'winter':
        costs = budget * 0.7
        is_hotel = True
elif 100 < budget <= 1000:
    location = 'Balkans'
    if season == 'summer':
        costs = budget * 0.4
        is_camp = True
    elif season == 'winter':
        costs = budget * 0.8
        is_hotel = True
elif budget > 1000:
    location = 'Europe'
    costs = budget * 0.9
    is_hotel = True

if is_hotel:
    print(f'Somewhere in {location}\n'
          f'Hotel - {costs:.2f}')
elif is_camp:
    print(f'Somewhere in {location}\n'
          f'Camp - {costs:.2f}')