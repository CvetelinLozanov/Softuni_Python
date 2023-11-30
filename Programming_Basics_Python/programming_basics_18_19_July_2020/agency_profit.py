company_name = input()
tickets_for_adults = int(input())
tickets_for_kids = int(input())
price_for_adult_tickets = float(input())
price_for_service = float(input())

price_for_kids_ticket = price_for_adult_tickets * 0.30
total_price = ((price_for_kids_ticket + price_for_service) * tickets_for_kids) + ((price_for_adult_tickets + price_for_service) * tickets_for_adults)
company_profit = total_price * 0.20

print(f'The profit of your agency from {company_name} tickets is {company_profit:.2f} lv.')