def naughty_or_nice_list(kids, *args, **kwargs):
    numbers = [kid[0] for kid in kids]
    names = [kid[1] for kid in kids]
    result = []
    nice_kids = []
    naughty_kids = []
    not_found_kids = []

    if args:
        for arg in args:
            number, group = arg.split('-')
            number = int(number)
            if numbers.count(number) > 1 or numbers.count(number) == 0:
                continue

            current_kid = [kid for kid in kids if kid[0] == number]
            if group == 'Nice':
                nice_kids.append(current_kid[0][1])
            elif group == 'Naughty':
                naughty_kids.append(current_kid[0][1])

            names.remove(current_kid[0][1])
            numbers.remove(current_kid[0][0])
            kids.remove(current_kid[0])

    if kwargs:
        for k, v in kwargs.items():
            if names.count(k) > 1 or names.count(k) == 0:
                continue

            current_kid = [kid for kid in kids if kid[1] == k]

            if v == 'Nice':
                nice_kids.append(current_kid[0][1])
            elif v == 'Naughty':
                naughty_kids.append(current_kid[0][1])

            kids.remove(current_kid[0])
            names.remove(current_kid[0][1])
            numbers.remove(current_kid[0][0])

    [not_found_kids.append(kid[1]) for kid in kids]

    if nice_kids:
        result.append(f"Nice: {', '.join(nice_kids)}")
    if naughty_kids:
        result.append(f"Naughty: {', '.join(naughty_kids)}")
    if not_found_kids:
        result.append(f"Not found: {', '.join(not_found_kids)}")

    return "\n".join(result)



print(naughty_or_nice_list(
    [
        (3, "Amy"),
        (1, "Tom"),
        (7, "George"),
        (3, "Katy"),
    ],
    "3-Nice",
    "1-Naughty",
    Amy="Nice",
    Katy="Naughty",
))


print(naughty_or_nice_list(
    [
        (7, "Peter"),
        (1, "Lilly"),
        (2, "Peter"),
        (12, "Peter"),
        (3, "Simon"),
    ],
    "3-Nice",
    "5-Naughty",
    "2-Nice",
    "1-Nice",
    ))


print(naughty_or_nice_list(
    [
        (6, "John"),
        (4, "Karen"),
        (2, "Tim"),
        (1, "Merry"),
        (6, "Frank"),
    ],
    "6-Nice",
    "5-Naughty",
    "4-Nice",
    "3-Naughty",
    "2-Nice",
    "1-Naughty",
    Frank="Nice",
    Merry="Nice",
    John="Naughty",
))