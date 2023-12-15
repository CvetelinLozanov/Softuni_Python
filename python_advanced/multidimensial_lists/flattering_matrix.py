matrix = [[int(el) for el in input().split(', ')] for i in range(int(input()))]

flattered_matrix = [num for el in matrix for num in el]

print(flattered_matrix)