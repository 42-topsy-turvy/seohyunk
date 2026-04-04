# BOJ 1238 파티

import heapq
import sys  

input = sys.stdin.readline
INF = float('inf')

N, M, X = map(int, input().split())
graph = [[] for _ in range(N+1)]
reverse_graph = [[] for _ in range(N+1)]
for _ in range(M):
    start, end, T = map(int, input().split())
    graph[start].append((end, T))
    reverse_graph[end].append((start, T))

    
def dijkstra(graph, start):
    n = len(graph)
    dist = [INF] * n
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
 
dist_to_X = dijkstra(reverse_graph, X) # X로 출발
dist_from_X = dijkstra(graph, X) # X에서 출발

max_time = 0
for i, j in zip(dist_to_X, dist_from_X):
    if i == INF or j == INF:
        continue
    max_time = max(max_time, i + j)
    
print(max_time)