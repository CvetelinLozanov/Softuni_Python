def words_sorting(*args):
    words = {}

    for arg in args:
        words[arg] = calculate_ascii_value(arg)

    values_sum = sum(words.values())
    sorted_words = sorted(words.items(), key=lambda x: -x[1] if values_sum % 2 == 1 else x[0])
    result = []

    for word, value in sorted_words:
        result.append(f"{word} - {value}")

    return '\n'.join(result)


def calculate_ascii_value(word):
    return sum([ord(ch) for ch in word])

print(
    words_sorting(
        'escape',
        'charm',
        'mythology'
  ))

print()

print(
    words_sorting(
        'escape',
        'charm',
        'eye'
  ))

print()

print(
    words_sorting(
        'cacophony',
        'accolade'
  ))