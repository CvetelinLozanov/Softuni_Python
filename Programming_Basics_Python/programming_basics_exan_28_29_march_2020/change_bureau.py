number_of_bitcoins = int(input())
chinese_yuan = float(input())
commission = float(input())

yuan_to_dollars = chinese_yuan * 0.15
dollars_to_leva = yuan_to_dollars * 1.76
bitcoin_to_leva = 1168 * number_of_bitcoins
total_euro = bitcoin_to_leva / 1.95 + dollars_to_leva / 1.95
total_euro *= 1 - commission / 100
print(f'{total_euro:.2f}')