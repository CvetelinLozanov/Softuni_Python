from collections import deque


milligrams_caffeine = deque([int(num) for num in input().split(', ')])
energy_drinks = deque([int(num) for num in input().split(', ')])

initial_caffeine = 0
max_caffeine = 300

while milligrams_caffeine and energy_drinks:
    current_caffeine = milligrams_caffeine.pop()
    current_energy_drink = energy_drinks.popleft()

    caffeine_calculation = current_caffeine * current_energy_drink

    if caffeine_calculation <= max_caffeine:
        initial_caffeine += caffeine_calculation
        max_caffeine -= caffeine_calculation

    else:
        energy_drinks.append(current_energy_drink)
        initial_caffeine -= 30
        max_caffeine += 30

        if initial_caffeine <= 0:
            initial_caffeine = 0
            max_caffeine = 300

if energy_drinks:
    print(f"Drinks left: {', '.join(map(str, energy_drinks))}")

else:
    print(f"At least Stamat wasn't exceeding the maximum caffeine.")

print(f"Stamat is going to sleep with {initial_caffeine} mg caffeine.")

