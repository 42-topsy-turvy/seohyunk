# BOJ 2206 벽 부수고 이동하기
from collections import deque
import sys
from pprint import pprint

input = sys.stdin.readline

N, M = map(int, input().split())
grid = [list(map(int, input().strip())) for _ in range(N)]
visited = [[[False] * 2 for _ in range(M)]for _ in range(N)]
visited[0][0][0] = True

def bfs(N, M, grid):
    dirs = [(0,1), (0, -1), (1, 0), (-1, 0)]
    queue = deque([(0, 0, 1, 0)])

    while queue:
        cx, cy, dist, broken = queue.popleft()
        if cx == N-1 and cy == M-1:
            return dist
        
        for dx, dy in dirs:
            nx, ny = dx + cx, dy + cy
            
            if 0 <= nx < N and 0 <= ny < M:
                if grid[nx][ny] == 0 and not visited[nx][ny][broken]:
                    visited[nx][ny][broken] = True
                    # print("========")
                    # pprint(visited)
                    queue.append((nx, ny, dist + 1, broken))
                
                elif grid[nx][ny] == 1 and broken == 0 and not visited[nx][ny][1]:
                    visited[nx][ny][1] = True
                    queue.append((nx, ny, dist + 1, 1))
             
    return -1

print(bfs(N, M, grid))