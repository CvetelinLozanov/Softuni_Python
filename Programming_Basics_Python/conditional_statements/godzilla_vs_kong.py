budget_for_film = float(input())
number_of_stats = int(input())
price_for_cloth_per_stat = float(input())

budget_for_film *= 0.9
costs_for_clothes = number_of_stats * price_for_cloth_per_stat

if number_of_stats > 150:
    costs_for_clothes *= 0.9
if costs_for_clothes > budget_for_film:
    print("Not enough money!\n"
      f"Wingard needs {costs_for_clothes - budget_for_film:.2f} leva more.")
else:
    print(f"Action!\n"
          f"Wingard starts filming with {budget_for_film - costs_for_clothes:.2f} leva left.")
