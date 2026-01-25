# BOJ 15664 N과 M(10)

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
numbers = list(map(int, input().split()))

numbers.sort()
result = []
visited = [False] * N

all = set()

def backtracking(depth, start):
	if depth == M:
		if tuple(result) not in all:
			print(*result)
			all.add(tuple(result))
		return
	
	for i in range(start, N):
		if visited[i]:
			continue

		visited[i] = True
		result.append(numbers[i])
		backtracking(depth + 1, i)	
		result.pop()
		visited[i] = False

backtracking(0, 0)
