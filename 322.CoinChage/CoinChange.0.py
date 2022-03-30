def change(amount, coins):
    if amount == 0:
        return 0
    elif coins[0] > amount:
        return change(amount, coins[1:])
    else: # coins[0] <= amount
        return change(amount - coins[0], coins) + 1


coins = list(map(int, input().split()))
amount = int(input())
coins.sort(reverse = True)
mincoins = change(amount, coins)
print(mincoins)
