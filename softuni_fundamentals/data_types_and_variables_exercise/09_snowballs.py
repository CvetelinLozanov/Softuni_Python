number_of_snowballs = int(input())

best_ball = 0
best_weight = 0
best_time_to_target = 0
best_quality = 0

for _ in range(number_of_snowballs):
    snowball_weight = int(input())
    time_to_target = int(input())
    snowball_quality = int(input())

    ball_value = (snowball_weight / time_to_target) ** snowball_quality

    if ball_value > best_ball:
        best_weight = snowball_weight
        best_time_to_target = time_to_target
        best_quality = snowball_quality
        best_ball = ball_value


print(f'{best_weight} : {best_time_to_target} = {int(best_ball)} ({best_quality})')



