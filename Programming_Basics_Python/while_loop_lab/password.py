name = input()
password = input()

while True:
    input_password = input()
    if input_password == password:
        print(f'Welcome {name}!')
        break
