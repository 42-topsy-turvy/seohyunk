# BOJ 11052 카드 구매하기

N = int(input())
cards = list(map(int, input().split()))
cards = [0] + cards
dp = [0] * (N + 1)
dp[1] = cards[1]
dp[2] = max(cards[1] * 2, cards[2])

for i in range(2, N+1):
    for j in range(1, i+1):
        dp[i] = max(dp[i], cards[j] + dp[i-j])

print(dp[N])
