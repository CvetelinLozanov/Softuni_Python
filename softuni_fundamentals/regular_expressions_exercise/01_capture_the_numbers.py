import re

text = ''
while True:
    line = input()
    if line:
        text += line + '\n'
    else:
        break

pattern = r'\d+'
compiled = re.compile(pattern, re.DOTALL | re.MULTILINE)
matches = compiled.findall(text)
print(" ".join(matches))
