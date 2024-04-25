from collections import deque


fireworks_effect = deque([int(num) for num in input().split(', ')])
explosives_power = deque([int(num) for num in input().split(', ')])

palm_firework = 0
willow_firework = 0
crossette_firework = 0
is_firework_crafted = False

while fireworks_effect and explosives_power:
    if fireworks_effect[0] <= 0:
        fireworks_effect.popleft()
        continue

    if explosives_power[-1] <= 0:
        explosives_power.pop()
        continue

    current_firework_effect = fireworks_effect[0]
    current_explosive_power = explosives_power[-1]
    firework_sum = current_firework_effect + current_explosive_power

    if firework_sum % 3 == 0 and not firework_sum % 5 == 0:
        palm_firework += 1
        is_firework_crafted = True

    elif firework_sum % 5 == 0 and not firework_sum % 3 == 0:
        willow_firework += 1
        is_firework_crafted = True

    elif firework_sum % 3 == 0 and firework_sum % 5 == 0:
        crossette_firework += 1
        is_firework_crafted = True

    if is_firework_crafted:
        fireworks_effect.popleft()
        explosives_power.pop()
        is_firework_crafted = False

    else:
        fireworks_effect[0] -= 1
        fireworks_effect.rotate(-1)

    if palm_firework >= 3 and willow_firework >= 3 and crossette_firework >= 3:
        print("Congrats! You made the perfect firework show!")
        break
else:
    print("Sorry. You can't make the perfect firework show.")

if fireworks_effect:
    print(f"Firework Effects left: {', '.join(map(str, fireworks_effect))}")
if explosives_power:
    print(f"Explosive Power left: {', '.join(map(str, explosives_power))}")

print(f"Palm Fireworks: {palm_firework}\nWillow Fireworks: {willow_firework}\nCrossette Fireworks: {crossette_firework}")