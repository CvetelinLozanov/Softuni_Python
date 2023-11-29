budget = float(input())

while True:
    actor_name = input()

    if actor_name == 'ACTION':
        break

    actor_name_length = len(actor_name)

    if actor_name_length > 15:
        budget -= budget * 0.20
        continue

    salary = float(input())

    if salary >= budget:
        print(f'We need {salary - budget:.2f} leva for our actors.')
        budget -= salary
        break

    budget -= salary

if budget > 0:
    print(f'We are left with {budget:.2f} leva.')
