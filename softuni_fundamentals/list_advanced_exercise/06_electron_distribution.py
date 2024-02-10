def electron_distribution():
    number_of_electrons = int(input())
    shell = []

    counter = 1
    while number_of_electrons > 0:
        max_electrons = 2 * (counter ** 2)
        if number_of_electrons > max_electrons:
            shell.append(max_electrons)
        else:
            shell.append(number_of_electrons)
            break
        number_of_electrons -= max_electrons
        counter += 1

    return shell


print(electron_distribution())