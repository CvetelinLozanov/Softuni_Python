name_of_actor = input()
points_from_academy = float(input())
number_of_evaluates = int(input())

points_of_actor = points_from_academy

for _ in range(number_of_evaluates):
    name_of_evaluator = input()
    points_of_evaluator = float(input())
    points_from_evaluator = (len(name_of_evaluator) * points_of_evaluator) / 2

    points_of_actor += points_from_evaluator

    if points_of_actor > 1250.5:
        print(f'Congratulations, {name_of_actor} got a nominee for leading role with {points_of_actor:.1f}!')
        break

else:
    print(f'Sorry, {name_of_actor} you need {1250.5 - points_of_actor:.1f} more!')