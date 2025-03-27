# BOJ 2294 동전 2

n, k = map(int, input().split())
coins=[]
dp = [0 for _ in range(k)]
cnt = 0

for _ in range(n):
    coins.append(int(input()))

coins.sort(reverse=True)
print(coins[0], k)

dp[0] = k // coins[0]

for i in range(1, n):
    for coin in coins:
        print(f'{dp[i-1]}  {k-coins[i-1]}')
        # dp[i] = min(dp[i-1]+(k-coins[i-1]*dp[i-1])//coins[i-1], dp[i])

# print(min(dp))