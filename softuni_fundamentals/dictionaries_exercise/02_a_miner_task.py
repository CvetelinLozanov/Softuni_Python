counter = 1
resources = {}
current_resource = ''

while True:
    command = input()

    if command == 'stop':
        break

    if counter % 2 != 0:
        current_resource = command
        if command not in resources:
            resources[command] = 0

    else:
        resources[current_resource] += int(command)
        current_resource = ''

    counter += 1

[print(f"{resource} -> {quantity}") for resource, quantity in resources.items()]

