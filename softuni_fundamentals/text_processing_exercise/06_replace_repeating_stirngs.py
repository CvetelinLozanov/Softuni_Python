def dup_char_remover(text):
    output = ""
    final_text = ""
    for c in text:
        if final_text != c:
            output = output + c
        final_text = c
    return output


text = input()
output = dup_char_remover(text)
print(output)