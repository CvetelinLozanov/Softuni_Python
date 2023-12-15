#rows = int(input())

test_matrix = [[int(j) for j in input().split(', ') if int(j) % 2 == 0] for i in range(int(input()))]

matrix = []

# for _ in range(rows):
#     matrix.append([int(x) for x in input().split(', ') if int(x) % 2 == 0])
#
print(test_matrix)