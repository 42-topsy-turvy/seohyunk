# BOJ 1261 알고스팟

import heapq
import sys

input = sys.stdin.readline
INF = float('inf')

M, N = map(int, input().split())
graph = [list(map(int, input().strip())) for _ in range(N)]

def dijkstra(graph):
    n, m = len(graph), len(graph[0])
    dist = [[INF] * m for _ in range(n)]
    dist[0][0] = 0
    heap = [(0, 0, 0)] # 벽 부순 횟수, x, y
    
    while heap:
        broken, x, y = heapq.heappop(heap) 
        
        if (x, y) == (n-1, m-1):
            return broken
        
        if broken > dist[x][y]:
            continue
        
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            nx, ny = x + dx, y + dy
            
            if 0 <= nx < n and 0 <= ny < m:
                cost = 1 if graph[nx][ny] == 1 else 0
                new_broken = broken + cost
                
                if new_broken < dist[nx][ny]:
                    dist[nx][ny] = new_broken
                    heapq.heappush(heap, (new_broken, nx, ny))
                    
    return dist[n-1][m-1]

print(dijkstra(graph))