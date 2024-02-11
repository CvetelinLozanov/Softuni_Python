from collections import deque


def increase_and_decrease_values(pokemons, removed_element):
    for index in range(len(pokemons)):
        if pokemons[index] <= removed_element:
            pokemons[index] += removed_element
        else:
            pokemons[index] -= removed_element


def processing_pokemnons():
    distance_to_pokemons = list(map(int, input().split()))
    sum_of_all_removed_items = 0
    element = 0

    while distance_to_pokemons:
        index = int(input())

        if index < 0:
            element = distance_to_pokemons.pop(0)
            if distance_to_pokemons:
                pokemon_to_insert = distance_to_pokemons[-1]
                distance_to_pokemons.insert(0, pokemon_to_insert)
                increase_and_decrease_values(distance_to_pokemons, element)

        elif index > len(distance_to_pokemons) - 1:
            element = distance_to_pokemons.pop()
            if distance_to_pokemons:
                distance_to_pokemons.append(distance_to_pokemons[0])
                increase_and_decrease_values(distance_to_pokemons, element)

        else:
            element = distance_to_pokemons.pop(index)
            increase_and_decrease_values(distance_to_pokemons, element)

        sum_of_all_removed_items += element

    return sum_of_all_removed_items


print(processing_pokemnons())