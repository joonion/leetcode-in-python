INF = 999999

def changemem(W, coins, memo):
    if W not in memo:
        if W == 0:
            memo[W] = 0
        else:
            memo[W] = INF
            for i in range(len(coins)):
                if coins[i] <= W:
                    memo[W] = min(memo[W], 
                                  changemem(W - coins[i], coins, memo) + 1)
    return memo[W]
    
def change(amount, coins):
    memo = {}
    ret = changemem(amount, coins, memo)
    return ret if ret < INF else -1
        
coins = list(map(int, input().split()))
amount = int(input())
coins.sort(reverse = True)
mincoins = change(amount, coins)
print(mincoins)