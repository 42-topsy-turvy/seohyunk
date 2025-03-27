# 가장 긴 증가하는 부분 수열 2

import sys

N = int(sys.stdin.readline().rstrip())
A_list = list(map(int, sys.stdin.readline().rstrip().split()))

dp = [N]
# for i in range(N):
#     dp[i] = 1
#     for j in range(i):
#         if(A_list[i] > A_list[j]):
#             dp[i] = max(dp[i], dp[j] + 1)

print(max(dp))