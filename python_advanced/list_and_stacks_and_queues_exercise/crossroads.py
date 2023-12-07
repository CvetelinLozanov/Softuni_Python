from collections import deque

initial_green_light_duration = int(input())
initial_free_window_duration = int(input())
cars_passed = 0
cars = deque()
command = input()
is_crash = False

while command != 'END':

    if command == 'green':
        green_light_duration = initial_green_light_duration
        free_window_duration = initial_free_window_duration
        while cars and green_light_duration > 0:
            car = cars.popleft()

            if len(car) <= green_light_duration:
                green_light_duration -= len(car)
                cars_passed += 1
                continue
            else:
                stuck_car = len(car) - green_light_duration

                if stuck_car <= free_window_duration:
                    cars_passed += 1
                    break
                else:
                    print(f'A crash happened!\n{car} was hit at {car[free_window_duration + green_light_duration]}.')
                    is_crash = True
                    break

    else:
        car_model = command
        cars.append(car_model)

    if is_crash:
        break

    command = input()

if not is_crash:
    print(f'Everyone is safe.\n{cars_passed} total cars passed the crossroads.')