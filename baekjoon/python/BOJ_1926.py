# BOJ 1926 그림

from collections import deque

n, m = map(int, input().split())
matrix = [list(map(int, input().split()))for _ in range(n)]

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

paint = []

def bfs(graph, a, b):
    cnt = 1
    queue = deque()
    queue.append((a, b))
    graph[a][b]=0

    while queue:
        x, y = queue.popleft() 
        for dir_x, dir_y in zip(dx, dy):
            nx=x+dir_x
            ny=y+dir_y
            if 0 <= nx < n and 0 <= ny < m and graph[nx][ny]==1:
                # print((nx, ny))
                graph[nx][ny]=0
                queue.append((nx, ny))
                cnt += 1

    return cnt 

for i in range(n):
    for j in range(m):
        if matrix[i][j] == 1:
            paint.append(bfs(matrix, i, j))

# print(paint)


if len(paint) == 0:
    print(len(paint))
    print(0)
else:
    print(len(paint))
    print(max(paint))