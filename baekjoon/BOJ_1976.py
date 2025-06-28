# BOJ 1976 여행 가자

from collections import deque

def BFS(graph, V):
    length = len(graph)
    visited = [False] * length
    queue = deque([V])
    visited[V] = True

    while queue:
        cur = queue.popleft()
        for i in range(length):
            if graph[cur][i] == 1 and not visited[i]:
                queue.append(i)
                visited[i] = True

    return visited

def main():
    N = int(input())
    M = int(input())
    connections = [list(map(int, input().split())) for _ in range(N)]
    plans = list(map(int, input().split()))
    
    plans = [p - 1 for p in plans]
    
    connected = BFS(connections, plans[0])
    return 'YES' if all(connected[plan] for plan in plans) else 'NO'

if __name__=='__main__':
    print(main())