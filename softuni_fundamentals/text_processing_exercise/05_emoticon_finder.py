text = input()

colon_count = text.count(':')
index_pos = 0
emojis = []

for _ in range(colon_count):
    index_of_colon = text.index(':', index_pos)
    emojis.append(text[index_of_colon: index_of_colon + 2])
    index_pos = index_of_colon + 1

print('\n'.join(emojis))