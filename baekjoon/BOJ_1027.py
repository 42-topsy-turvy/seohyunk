# BOJ 1027 고층 건물
import sys

input = sys.stdin.readline

N = int(input())
buildings = list(map(int, input().split()))

result = 0

for i in range(N):
    right_temp = 1
    left_temp = 0
    max_right = buildings[i+1] - buildings[i]
    min_left = float("inf")
    if i < N - 1:
        for j in range(i + 2, N):
            slope = (buildings[j] - buildings[i]) / (j - i)
            if slope > max_right:
                max_right = slope
                right_temp += 1
    if i > 0:
        for j in range(i - 1, -1, -1):
            slope = (buildings[j] - buildings[i]) / (j - i)
            if slope < min_left:
                min_left = slope
                left_temp += 1
    result = max(result, right_temp + left_temp)

print(result)
