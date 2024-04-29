from collections import deque

materials = deque([int(material) for material in input().split()])
magic_level = deque([int(magic) for magic in input().split()])

gifts = {
    "Gemstone": 0,
    "Porcelain Sculpture": 0,
    "Gold": 0,
    "Diamond Jewellery": 0
}

gemstone = 0
porcelain_sculpture = 0
gold = 0
diamond_jewellery = 0

while materials and magic_level:
    product_sum = materials[-1] + magic_level[0]

    if product_sum < 100:
        if product_sum % 2 == 0:
            materials[-1] *= 2
            magic_level[0] *= 3
            product_sum = materials[-1] + magic_level[0]
        else:
            product_sum *= 2
    elif product_sum > 499:
        product_sum /= 2

    if 100 <= product_sum < 200:
        gifts['Gemstone'] += 1
    elif 200 <= product_sum < 300:
        gifts['Porcelain Sculpture'] += 1
    elif 300 <= product_sum < 400:
        gifts['Gold'] += 1
    elif 400 <= product_sum < 500:
        gifts['Diamond Jewellery'] += 1

    materials.pop()
    magic_level.popleft()

if (gifts["Gemstone"] > 0 and gifts["Porcelain Sculpture"] > 0) or (gifts["Gold"] > 0 and gifts["Diamond Jewellery"] > 0):
    print("The wedding presents are made!")
else:
    print("Aladdin does not have enough wedding presents.")

if materials:
    print(f"Materials left: {', '.join(map(str, materials))}")
if magic_level:
    print(f"Magic left: {', '.join(map(str, magic_level))}")

for k, v in sorted(gifts.items(), key=lambda x: x[0]):
    if v >= 1:
        print(f"{k}: {v}")

