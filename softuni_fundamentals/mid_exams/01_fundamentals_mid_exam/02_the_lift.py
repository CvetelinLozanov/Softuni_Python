people = int(input())
lift = [int(x) for x in input().split(' ')]

empty_spots = len(lift) * 4

for i in range(len(lift)):
    for x in range(4):
        if lift[i] < 4:
            if people > 0:
                lift[i] += 1
                people -= 1
            else:
                break
mapping = list(map(str, lift))

if sum(lift) < empty_spots:
    print(f'The lift has empty spots!')
    print(" ".join(mapping))
elif people > 0:
    print(f"There isn't enough space! {people} people in a queue!")
    print(" ".join(mapping))
elif people == 0:
    print(" ".join(mapping))