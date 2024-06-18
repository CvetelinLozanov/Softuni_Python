def sum_coins(coins, target):
    coins.sort(reverse=True)
    index = 0
    collected_coins = {}

    while target != 0 and index < len(coins):
        coins_to_take = target // coins[index]
        target %= coins[index]

        if coins_to_take > 0:
            collected_coins[coins[index]] = coins_to_take

        index += 1

    if target != 0:
        return "Error"

    result = f"Number of coins to take: {sum(collected_coins.values())}\n"
    result += '\n'.join([f"{coins_number} coin(s) with value {coin}" for coin, coins_number in collected_coins.items()])
    return result.strip()


coins = [int(num) for num in input().split(', ')]
target = int(input())
print(sum_coins(coins, target))