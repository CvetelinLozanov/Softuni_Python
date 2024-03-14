import re


text = input()

variable_pattern = r'\b_[A-Za-z0-9]+\b'
variable_matches = re.findall(variable_pattern, text)

variable_name_pattern = r'[A-Za-z0-9]+'
print(','.join(re.search(variable_name_pattern, variable).group() for variable in variable_matches))