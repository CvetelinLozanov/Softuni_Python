num = int(input())

chemical_elements = set()

for _ in range(num):
    [chemical_elements.add(element) for element in input().split()]

[print(element) for element in chemical_elements]
#print(*chemical_elements, sep='\n')
