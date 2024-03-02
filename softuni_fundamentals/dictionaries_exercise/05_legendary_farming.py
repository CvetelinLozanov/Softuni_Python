def process_materials(junk, materials, material, quantity):
    if material in ['shards', 'fragments', 'motes']:
        item = materials[material]['item']
        materials[material]['amount'] += quantity
        if materials[material]['amount'] >= 250:
            materials[material]['amount'] = abs(250 - materials[material]['amount'])
            print(f'{item} obtained!')
            return True
    else:
        if material not in junk:
            junk[material] = 0
        junk[material] += quantity

    return False


def print_result(materials, junk):
    print(f"shards: {materials['shards']['amount']}\n"
          f"fragments: {materials['fragments']['amount']}\n"
          f"motes: {materials['motes']['amount']}")
    for item, quantity in junk.items():
        print(f'{item}: {quantity}')


materials = {
    'shards': {'amount': 0, 'item': 'Shadowmourne'},
    'fragments': {'amount': 0, 'item': 'Valanyr'},
    'motes': {'amount': 0, 'item': 'Dragonwrath'}
}
junk = {}
is_end = False

while True:
    materials_info = input().split()

    for index in range(0, len(materials_info), 2):
        material = materials_info[index + 1].lower()
        quantity = int(materials_info[index])

        is_end = process_materials(junk, materials, material, quantity)

        if is_end:
            break

    if is_end:
        break


print_result(materials, junk)
