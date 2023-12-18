def age_assignment(*args, **kwargs):
    dict = {}
    for k, v in kwargs.items():
        for name in args:
            if name.startswith(k):
                dict[name] = v

    sorted_dict = sorted(dict.items(), key=lambda x: x[0])
    result = ''
    for name, age in sorted_dict:
        result += f'{name} is {age} years old.\n'

    return result

print(age_assignment("Peter", "George", G=26, P=19))