voucher = float(input())

tickets = 0
other_buys = 0

buy = input()

while buy != 'End':
    buy_length = len(buy)

    if buy_length > 8:
        ticket_price = ord(buy[0]) + ord(buy[1])

        if ticket_price <= voucher:
            tickets += 1
            voucher -= ticket_price
        else:
            break
            
    else:
        buy_price = ord(buy[0])

        if buy_price <= voucher:
            other_buys += 1
            voucher -= buy_price
        else:
            break

    buy = input()

print(tickets)
print(other_buys)