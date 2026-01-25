# BOJ 15657 N과 M(8)

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
numbers = list(map(int, input().split()))

numbers.sort()
result = []

def backtracking(depth, start):
	if depth == M:
		print(*result)
		return

	for i in range(start, N):
		result.append(numbers[i])
		backtracking(depth + 1, i)
		result.pop()

backtracking(0, 0)
