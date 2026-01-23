# BOJ 15655 N과 M(6)

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
numbers = list(map(int, input().split()))
numbers.sort()

result = []
visited = [False] * N

def backtracking(depth, start):
    if depth == M:
        print(*result)
        return
    
    for i in range(start, N):
        if visited[i]:
            continue
        
        visited[i] = True
        result.append(numbers[i])
        backtracking(depth + 1, i + 1)
        visited[i] = False
        result.pop()

backtracking(0, 0)
