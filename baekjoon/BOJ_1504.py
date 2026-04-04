# BOJ 1504 특정한 최단 경로

import heapq
import sys

input = sys.stdin.readline
N, E = map(int, input().split())

graph = [[] for _ in range(N+1)] # 1번부터 N번까지 사용

for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))
    
v1, v2 = map(int, input().split())
# print(graph)

def dijkstra(graph, start):
    n = len(graph)
    dist = [float('inf')] * n
    dist[start] = 0
    
    heap = [(0, start)]
    
    while heap:
        d, node = heapq.heappop(heap)
        
        if d > dist[node]:
            continue
        
        for next_node, cost in graph[node]:
            new_dist = d + cost
            
            if new_dist < dist[next_node]:
                dist[next_node] = new_dist
                heapq.heappush(heap, (new_dist, next_node))
                
    return dist

dist_1 = dijkstra(graph, 1) # 1에서 출발
dist_v1 = dijkstra(graph, v1)   # v1에서 출발
dist_v2 = dijkstra(graph, v2)   # v2에서 출발

# 1 -> v1 -> v2 -> N
path1 = dist_1[v1] + dist_v1[v2] + dist_v2[N]
# 1 -> v2 -> v1 -> N
path2 = dist_1[v2] + dist_v2[v1] + dist_v1[N]

result = min(path1, path2)
if result == float('inf'):
    print(-1)
else:
    print(result)