import re


def get_process_group(barcode_for_checking_: str):
    pattern = r'\d+'
    digits = re.findall(pattern, barcode_for_checking_)

    if digits:
        return ''.join(digits)
    else:
        return '00'


number_of_barcodes = int(input())
pattern = r'([@][#]{1,})([A-Z][a-zA-Z0-9]{4,}[A-Z])([@][#]{1,})'
message = ''

for _ in range(number_of_barcodes):
    barcode = input()
    matches = re.findall(pattern, barcode)
    if matches:
        barcode_for_checking = matches[0][1]
        process_group = get_process_group(barcode_for_checking)
        message = f'Product group: {process_group}'
    else:
        message = 'Invalid barcode'

    print(message)
