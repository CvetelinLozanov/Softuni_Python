def main():
    pirating_days = int(input())
    daily_plunder = int(input())
    expected_plunder = int(input())
    collected_plunder = 0

    for day in range(1, pirating_days + 1):
        collected_plunder += daily_plunder

        if day % 3 == 0:
            collected_plunder += daily_plunder * 0.5

        if day % 5 == 0:
            collected_plunder *= 0.70

    if collected_plunder >= expected_plunder:
        print(f'Ahoy! {collected_plunder:.2f} plunder gained.')
    else:
        remaining_percentage = (collected_plunder / expected_plunder) * 100
        print(f'Collected only {remaining_percentage:.2f}% of the plunder.')


if __name__ == '__main__':
    main()