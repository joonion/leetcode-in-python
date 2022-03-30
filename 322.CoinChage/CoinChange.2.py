def change(amount, coins):
    INF = amount + 1
    dp = [INF] * (INF)
    dp[0] = 0
    for W in range(1, amount + 1):
        for i in range(len(coins)):
            if coins[i] <= W:
                dp[W] = min(dp[W], dp[W - coins[i]] + 1)
    return dp[amount] if dp[amount] < INF else -1

coins = list(map(int, input().split()))
amount = int(input())
coins.sort(reverse = True)
mincoins = change(amount, coins)
print(mincoins)
