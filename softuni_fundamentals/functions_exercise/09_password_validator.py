from string import ascii_lowercase, ascii_uppercase, digits

def password_validator(password: str):
    is_password_valid = True

    if not check_password_length(password):
        is_password_valid = False
        print('Password must be between 6 and 10 characters')

    if not check_if_password_have_only_letters_and_digits(password):
        is_password_valid = False
        print('Password must consist only of letters and digits')

    if not check_if_password_have_at_least_two_digits(password):
        is_password_valid = False
        print('Password must have at least 2 digits')

    if is_password_valid:
        print('Password is valid')


def check_password_length(password: str):
    return 6 <= len(password) <= 10


def check_if_password_have_only_letters_and_digits(password: str):
    for char in password:
        if char not in digits and char not in ascii_lowercase and char not in ascii_uppercase:
            return False
    return True


def check_if_password_have_at_least_two_digits(password: str):
    digits_counter = len([char for char in password if char.isdigit()])
    return digits_counter >= 2


password = input()
password_validator(password)