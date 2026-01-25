# BOJ 15665 N과 M(11)

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
numbers = list(map(int, input().split()))

result = []
numbers.sort()
all = set()

def backtracking(depth, start):
	if depth == M:
		if tuple(result) not in all:
			print(*result)
			all.add(tuple(result))
		return

	for i in range(N):
		result.append(numbers[i])
		backtracking(depth + 1, i + 1)
		result.pop()

backtracking(0, 0)	
