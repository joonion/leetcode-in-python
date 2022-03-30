INF = 999999

def change(amount, coins):
    if amount == 0:
        return 0
    else:
        W = INF
        for coin in coins:
            if coin <= amount:
                W = min(W, change(amount - coin, coins) + 1)
        return W if W < INF else - 1

coins = list(map(int, input().split()))
amount = int(input())
coins.sort(reverse = True)
mincoins = change(amount, coins)
print(mincoins)
