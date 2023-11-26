training_height = int(input())
jump_counter = 0
unsuccessful_jump_counter = 0
target = training_height - 30
is_unsuccessful = False

while training_height >= target:
    tisho_jumps = int(input())

    if tisho_jumps > target:
        target += 5
        jump_counter += 1

    else:
        for _ in range(3):
            if tisho_jumps > target:
                target += 5
                jump_counter += 1
                break

            else:
                unsuccessful_jump_counter += 1
                jump_counter += 1
            if unsuccessful_jump_counter == 3:
                is_unsuccessful = True
                break

            tisho_jumps = int(input())

    if is_unsuccessful:
        print(f'Tihomir failed at {target}cm after {jump_counter} jumps.')
        break
    unsuccessful_jump_counter = 0

else:
    print(f'Tihomir succeeded, he jumped over {training_height}cm after {jump_counter} jumps.')
