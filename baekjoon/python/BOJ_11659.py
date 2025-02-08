# BOJ 11659 구간 합 구하기 4

import sys
input = sys.stdin.readline
N, M = map(int, input().split())
nums = list(map(int, input().split()))

cum_sums = [0]

for i in range(N):
    cum_sums.append(cum_sums[i]+nums[i])

for _ in range(M):
    i, j = map(int, input().split())
    print(cum_sums[j]-cum_sums[i-1])