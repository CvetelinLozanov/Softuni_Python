loan = float(input())
statues = loan * 0.70
catering = statues * 0.85
sound = catering / 2

total_sum = statues + catering + sound + loan
print(f'{total_sum:.2f}')