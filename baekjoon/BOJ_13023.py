# BOJ 13023 ABCDE

import sys

input = sys.stdin.readline

N, M = map(int, input().split())
graph = [[] for _ in range(N)]
visited = [False] * N

for _ in range(M):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

    
def backtracking(node, depth):
    if depth == 5:
        return True
    
    for next_node in graph[node]:
        if not visited[next_node]:
            visited[next_node] = True
            if backtracking(next_node, depth + 1):
                return True
            visited[next_node] = False
    
    return False

for i in range(N):
    visited[i] = True
    if backtracking(i, 1):
        print(1)
        exit()
    visited[i] = False

print(0)