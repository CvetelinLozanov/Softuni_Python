from collections import deque

flowers = {
    "rose": "rose",
    "tulip": "tulip",
    "lotus": "lotus",
    "daffodil": "daffodil"
}

vowels = deque([letter for letter in input().split()])
consonants = deque([letter for letter in input().split()])
is_flower_found = False
found_flower = ''

while vowels and consonants:
    current_vowel = vowels.popleft()
    current_consonant = consonants.pop()

    for flower in flowers:
        if current_vowel in flower and current_vowel in flowers[flower]:
            flowers[flower] = flowers[flower].replace(current_vowel, '')

        if current_consonant in flower and current_consonant in flowers[flower]:
            flowers[flower] = flowers[flower].replace(current_consonant, '')

        if len(flowers[flower]) == 0:
            found_flower = flower
            is_flower_found = True

    if is_flower_found:
        print(f"Word found: {found_flower}")
        break
else:
    print("Cannot find any word!")

if vowels:
    print(f"Vowels left: {' '.join(vowels)}")
if consonants:
    print(f"Consonants left: {' '.join(consonants)}")
