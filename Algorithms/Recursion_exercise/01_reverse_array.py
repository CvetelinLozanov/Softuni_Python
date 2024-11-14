def reverse_array(idx, elements):
    if idx == len(elements) // 2:
        return
    swp_index = len(elements) - 1 - idx
    elements[idx], elements[swp_index] = elements[swp_index], elements[idx]
    reverse_array(idx + 1, elements)


elements = input().split()

reverse_array(0, elements)

print(*elements)