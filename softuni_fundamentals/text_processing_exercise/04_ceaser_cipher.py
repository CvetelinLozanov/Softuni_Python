text = input()

encrypted_word = ''

for ch in text:
    encrypted_word += chr(ord(ch) + 3)

print(encrypted_word)