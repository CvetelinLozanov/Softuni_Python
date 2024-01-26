num = int(input())
searched_word = input()
full_text = []

for _ in range(num):
    text = input()
    full_text.append(text)

result = [sentence for sentence in full_text if searched_word in sentence]
print(full_text)
print(result)
