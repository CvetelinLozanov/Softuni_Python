word = input()
final_word = [ch for ch in word if ch.lower() not in ['a', 'o', 'u', 'e', 'i']]
print(''.join(final_word))