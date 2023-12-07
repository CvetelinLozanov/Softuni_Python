from collections import deque

price_for_bullet = int(input())
size_of_gun_barrel = int(input())
bullets = deque([int(bullet) for bullet in input().split()])
locks = deque([int(lock) for lock in input().split()])
value_of_intelligence = int(input())

shots_counter = 0
total_shots_counter = 0

while locks and bullets:
    lock = locks[0]

    while bullets:
        bullet = bullets.pop()

        if lock >= bullet:
            shots_counter += 1
            total_shots_counter += 1
            print('Bang!')
            locks.popleft()
            if shots_counter == size_of_gun_barrel and bullets:
                shots_counter = 0
                print('Reloading!')
            break

        else:
            print('Ping!')
            shots_counter += 1
            total_shots_counter += 1

        if shots_counter == size_of_gun_barrel and bullets:
            shots_counter = 0
            print('Reloading!')

costs_for_bullets = price_for_bullet * total_shots_counter

if not locks:
    print(f'{len(bullets)} bullets left. Earned ${value_of_intelligence - costs_for_bullets}')
elif not bullets:
    print(f'Couldn\'t get through. Locks left: {len(locks)}')

# from collections import deque
# bullet_price = int(input())
# size_barrel = int(input())
#
# bullets = input().split(' ')
# bullets = deque([int(item) for item in bullets])
#
# org_bullets = deque(bullets)
#
# locks = input().split(' ')
# locks = deque([int(item) for item in locks])
#
# intelligence = int(input())
# shoot = 0
#
# while bullets and locks:
#     if bullets and shoot == size_barrel:
#         print(f'Reloading!')
#         shoot = 0
#     if bullets[-1] <= locks[0]:
#         print('Bang!')
#         bullets.pop()
#         locks.popleft()
#         shoot += 1
#     else:
#         print('Ping!')
#         bullets.pop()
#         shoot += 1
#
# if bullets and shoot == size_barrel:
#     print(f'Reloading!')
#     shoot = 0
#
# if locks:
#     print(f"Couldn't get through. Locks left: {len(locks)}")
# else:
#     cost = (len(org_bullets) - len(bullets)) * bullet_price
#     profit = intelligence - cost
#     print(f"{len(bullets)} bullets left. Earned ${profit}")
