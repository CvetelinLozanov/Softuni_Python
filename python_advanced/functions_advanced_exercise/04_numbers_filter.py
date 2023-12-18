def even_odd_filter(**kwargs):
    for k, v in kwargs.items():
        if k == 'even':
            kwargs[k] = list(filter(lambda x: x % 2 == 0, kwargs[k]))
        else:
            kwargs[k] = list(filter(lambda x: x % 2 != 0, kwargs[k]))
    sorted_dict = dict(sorted(kwargs.items(), key=lambda kvp: -len(kvp[1])))

    return sorted_dict


print(even_odd_filter(
    odd=[1, 2, 3, 4, 10, 5],
    even=[3, 4, 5, 7, 10, 2, 5, 5, 2],
))