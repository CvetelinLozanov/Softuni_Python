number_of_students = int(input())

dict = {}

for _ in range(number_of_students):
    name, grade = input().split()
    if name not in dict:
        dict[name] = []
    dict[name].append(float(grade))

for name, grades in dict.items():
    grades_result = ' '.join([f'{grade:.2f}' for grade in grades])

    print(f'{name} -> {grades_result} (avg: {sum(grades)/ len(grades):.2f})')