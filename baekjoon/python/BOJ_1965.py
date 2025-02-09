# BOJ 1965 상자넣기

n = int(input())
boxes = list(map(int, input().split()))
length = len(boxes)

dp = [1] * length

for i in range(length):
    for j in range(i):
        if boxes[j] < boxes[i]:
            dp[i] = max(dp[j]+1, dp[i])

print(max(dp))