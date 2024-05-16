from collections import deque


textiles = deque([int(num) for num in input().split()])
medicaments = deque([int(num) for num in input().split()])
items = {
    30: "Patch",
    40: "Bandage",
    100: "MedKit"
}
created_items = {}

while textiles and medicaments:
    current_textile = textiles.popleft()
    current_medicament = medicaments.pop()
    combined_sum = current_textile + current_medicament

    if combined_sum in items:
        if items[combined_sum] not in created_items:
            created_items[items[combined_sum]] = 0

        created_items[items[combined_sum]] += 1

    elif combined_sum > 100:
        if items[100] not in created_items:
            created_items[items[100]] = 0
        created_items[items[100]] += 1
        remaining_value = combined_sum - 100
        medicaments[-1] += remaining_value
    else:
        current_medicament += 10
        medicaments.append(current_medicament)

if not textiles and not medicaments:
    print("Textiles and medicaments are both empty.")

elif not textiles:
    print("Textiles are empty.")

elif not medicaments:
    print("Medicaments are empty.")

sorted_items = sorted(created_items.items(), key=lambda x: (-x[1], x[0]))

[print(f"{k} - {v}") for k, v in sorted_items]


if medicaments:
    print(f"Medicaments left: {', '.join(map(str, reversed(medicaments)))}")

if textiles:
    print(f"Textiles left: {', '.join(map(str, textiles))}")


