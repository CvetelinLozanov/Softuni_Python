usernames = input().split(', ')
valid_names = []
is_len_valid = False
contains_letters_and_numbers = False
hyphens = False
underscores = False

for user in usernames:
    if 3 <= len(user) <= 16:
        is_len_valid = True
        if user.isalnum():
            valid_names.append(user)
        else:
            for ch in user:
                if ch == '-' or ch == '_':
                    valid_names.append(user)


print('\n'.join(valid_names))