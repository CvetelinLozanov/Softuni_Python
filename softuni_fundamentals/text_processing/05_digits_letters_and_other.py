text = input()

digits = ''
letters = ''
other_characters = ''

for ch in text:
    if ch.isdigit():
        digits += ch
    elif ch.isalpha():
        letters += ch
    else:
        other_characters += ch

print(digits)
print(letters)
print(other_characters)