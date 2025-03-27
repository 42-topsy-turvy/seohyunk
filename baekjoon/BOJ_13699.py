# BOJ 13699 점화식
# Dynamic Programming 이용

import sys
n = int(sys.stdin.readline())
dp = [1] + ([0] * (n))

# [1][0][0][0][0][0] ... [0] -> 구할 값
def recursive(n):
    if dp[n] != 0:
        return dp[n]
    for i in range(n // 2):
        dp[n] += recursive(i) * recursive(n - 1 - i)
    dp[n] *= 2
    if n % 2 == 1:
        dp[n] += recursive(n // 2) ** 2
    return dp[n]

print(recursive(n))