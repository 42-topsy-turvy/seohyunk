# BOJ 11053 가장 긴 증가하는 부분 수열

N = int(input())
nums = list(map(int, input().split()))
length = len(nums)

dp = [1] * length

for i in range(length):
    for j in range(i):
        if nums[j] < nums[i]:
            dp[i] = max(dp[j]+1, dp[i])
print(dp)
print(max(dp))
