def list_manipulator(array, *args):
    new_list = []
    command = args[0]
    placement = args[1]
    numbers = list(args[2:])
    if command == 'add' and placement == 'beginning':
        new_list = numbers + array
    elif command == 'add' and placement == 'end':
        new_list = array + numbers
    elif command == 'remove' and placement == 'beginning':
        if numbers:
            new_list = array[numbers[0]:]
        else:
            new_list = array[1:]
    elif command == 'remove' and placement == 'end':
        if numbers:
            new_list = array[:-numbers[0]]
        else:
            new_list = array[:-1]

    return new_list


print(list_manipulator([1,2,3], "remove", "end"))
print(list_manipulator([1,2,3], "remove", "beginning"))
print(list_manipulator([1,2,3], "add", "beginning", 20))
print(list_manipulator([1,2,3], "add", "end", 30))
print(list_manipulator([1,2,3], "remove", "end", 2))
print(list_manipulator([1,2,3], "remove", "beginning", 2))
print(list_manipulator([1,2,3], "add", "beginning", 20, 30, 40))
print(list_manipulator([1,2,3], "add", "end", 30, 40, 50))