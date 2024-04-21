from collections import deque


bomb_effects = deque([int(bomb) for bomb in input().split(', ')])
bomb_casing = deque([int(bomb) for bomb in input().split(', ')])
dathura_bombs = 0
cherry_bombs = 0
smoke_decoy_bombs = 0
# bombs = {
#     "dathura": 0,
#     "cherry": 0,
#     "smoke_decoy": 0
# }

while bomb_effects and bomb_casing:
    is_bomb_crafted = True
    current_bomb_effect = bomb_effects[0]
    current_bomb_casing = bomb_casing[-1]
    current_bomb_sum = current_bomb_casing + current_bomb_effect

    if current_bomb_sum == 40:
        dathura_bombs += 1

    elif current_bomb_sum == 60:
        cherry_bombs += 1

    elif current_bomb_sum == 120:
        smoke_decoy_bombs += 1

    else:
        bomb_casing[-1] -= 5
        is_bomb_crafted = False

    if is_bomb_crafted:
        bomb_effects.popleft()
        bomb_casing.pop()

    if cherry_bombs >= 3 and dathura_bombs >= 3 and smoke_decoy_bombs >= 3:
        print("Bene! You have successfully filled the bomb pouch!")
        break
else:
    print("You don't have enough materials to fill the bomb pouch.")

if not bomb_effects:
    print("Bomb Effects: empty")
else:
    print(f"Bomb Effects: {', '.join(map(str,bomb_effects))}")
if not bomb_casing:
    print("Bomb Casings: empty")
else:
    print(f"Bomb Casings: {', '.join(map(str,bomb_casing))}")

print(f"Cherry Bombs: {cherry_bombs}\nDatura Bombs: {dathura_bombs}\nSmoke Decoy Bombs: {smoke_decoy_bombs}")
