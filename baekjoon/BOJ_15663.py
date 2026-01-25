# BOJ 15663 N과 M(9)

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
numbers = list(map(int, input().split()))

numbers.sort()
result = []
visited = [False] * N
all = set()

def backtracking(depth):
	if depth == M:
		if tuple(result) not in all:
			print(*result)
			all.add(tuple(result))
		return

	for i in range(N):
		if visited[i]:
			continue
		
		result.append(numbers[i])
		visited[i] = True
		backtracking(depth + 1)
		result.pop()
		visited[i] = False

backtracking(0)
