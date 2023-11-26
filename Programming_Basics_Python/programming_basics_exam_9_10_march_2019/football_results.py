win_counter = 0
loss_counter = 0
drawn_counter = 0

for _ in range(3):
    result = input()
    team_a_goals = int(result[0])
    team_b_goals = int(result[2])

    if team_a_goals > team_b_goals:
        win_counter += 1

    elif team_a_goals == team_b_goals:
        drawn_counter += 1

    elif team_a_goals < team_b_goals:
        loss_counter += 1

print(f'Team won {win_counter} games.')
print(f'Team lost {loss_counter} games.')
print(f'Drawn games: {drawn_counter}')