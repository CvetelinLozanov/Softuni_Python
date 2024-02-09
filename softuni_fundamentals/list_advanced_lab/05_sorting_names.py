def sorting_names():
    names = input().split(', ')
    sorted_names = sorted(names, key=lambda n: (-len(n), n))
    return sorted_names


print(sorting_names())