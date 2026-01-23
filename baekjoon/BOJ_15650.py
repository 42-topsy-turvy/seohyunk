# BOJ 15650 N과 M(2)

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
result = []
visited = [False] * (N+1)
def backtracking(depth, start):
    if depth == M:
        print(*result)
        return
    
    for i in range(start, N+1):
        if visited[i]:
            continue
        
        visited[i] = True
        result.append(i)
        backtracking(depth + 1, i + 1)
        visited[i] = False
        result.pop()

backtracking(0, 1)