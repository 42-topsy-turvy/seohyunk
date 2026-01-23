# BOJ 15652 N과 M(4)

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
result = []

def backtracking(depth, start):
	if depth == M:
		print(*result)
		return
	for i in range(start, N+1):
		result.append(i)
		backtracking(depth + 1, i)
		result.pop()

backtracking(0, 1)
