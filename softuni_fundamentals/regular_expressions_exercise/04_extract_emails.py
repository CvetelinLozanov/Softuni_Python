import re

text = input()
pattern = r'(^|(?<=\s))(([a-zA-Z0-9]+)([\.\-_]?)([A-Za-z0-9]+)(@)([a-zA-Z]+([\.\-][A-Za-z]+)+))(\b|(?=\s))'

matches = re.finditer(pattern, text)

[print(match.group()) for match in matches]