# BOJ 1697 숨바꼭질

from collections import deque

N, K = map(int, input().split())

def bfs():
    queue = deque([(N, 0)])
    visited = [False] * 100001
    visited[N] = True
    while queue:
        node, time = queue.popleft()
        visited[node] = True
        if node == K:
            return time
        for next_node in (node - 1, node + 1, 2 * node):
            if 0 <= next_node <= 100000 and not visited[next_node]:
                visited[next_node] = True
                queue.append((next_node, time + 1))

if N == K:
    print(0)
else:
    print(bfs())
