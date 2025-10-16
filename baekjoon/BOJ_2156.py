# BOJ 2156 포도주 시식

n = int(input())
glasses = []
for _ in range(n):
    glasses.append(int(input()))

dp = [0] * n

if n == 1:
    dp[0] = glasses[0]
elif n == 2:
    dp[0] = glasses[0]
    dp[1] = glasses[0] + glasses[1]
else:
    dp[0] = glasses[0]
    dp[1] = glasses[0] + glasses[1]
    dp[2] = max(
        glasses[0] + glasses[2],
        glasses[1] + glasses[2],
        glasses[0] + glasses[1],
    )

    for i in range(3, n):
        dp[i] = max(
            dp[i - 2] + glasses[i],
            dp[i - 3] + glasses[i - 1] + glasses[i],
            dp[i - 1],
        )

print(max(dp))

# 범위를 잘 확인하자