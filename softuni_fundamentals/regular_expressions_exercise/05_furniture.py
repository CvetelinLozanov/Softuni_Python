# 75/100 just for example with Dictionary maybe there is a test with multiple products with same name
# import re
# from typing import Dict
#
#
# def process_furniture(furniture_info: Dict[str, float], text: str):
#     pattern = r'>>([A-Za-z]+)<<([0-9]+\.?[0-9]+?)!([0-9]+)\b'
#     matches = re.finditer(pattern, text)
#
#     for match in matches:
#         furniture_name = match.group(1)
#         furniture_price = float(match.group(2))
#         furniture_quantity = float(match.group(3))
#         total_price = furniture_price * furniture_quantity
#
#         if furniture_name not in furniture_info:
#             furniture_info[furniture_name] = 0
#
#         furniture_info[furniture_name] += total_price
#     return furniture_info
#
#
# def print_result(furniture_info: Dict[str, float]):
#     print('Bought furniture:')
#     [print(fur_name) for fur_name in furniture_info.keys()]
#     print(f'Total money spend: {sum(furniture_info.values()):.2f}')
#
#
# def main():
#     furniture_info = {}
#
#     while True:
#         text = input()
#
#         if text == 'Purchase':
#             break
#
#         furniture_info = process_furniture(furniture_info, text)
#
#     print_result(furniture_info)
#
#
# if __name__ == '__main__':
#     main()


import re

command = input()

forniture_list = []
total_price = 0

while command != 'Purchase':
    rex = r'>>([A-Za-z]+)<<([0-9]+\.?[0-9]+?)!([0-9]+)\b'
    matches = re.finditer(rex, command)
    for match in matches:
        furniture = match.group(1)
        price = match.group(2)
        quantity = match.group(3)

        forniture_list.append(furniture)

        total_price += float(price) * float(quantity)

    command = input()


print(f'Bought furniture:')
for forni in forniture_list:
    print(forni)
print(f'Total money spend: {total_price:.2f}')