def repeat_string(text: str, repeat: int) -> str:
    return text * repeat


text = input()
repeat_times = int(input())
print(repeat_string(text, repeat_times))