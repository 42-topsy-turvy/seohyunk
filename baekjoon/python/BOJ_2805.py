# 2805 나무 자르기

import sys
N, M = map(int, sys.stdin.readline().split())
trees = list(map(int, sys.stdin.readline().split()))

# 1 ~ 제일 높은 나무
# 이분 탐색
start, end = 1, max(trees)
while start <= end:
    mid = (start + end) // 2
    sum = 0
    for tree in trees:
        if tree >= mid:
            sum += tree - mid
    if sum >= M:
        start = mid + 1
    else:
        end = mid - 1
print(end)
