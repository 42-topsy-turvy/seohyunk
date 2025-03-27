# BOJ 14502 연구소

from itertools import combinations
from collections import deque

def get_blank_list(matrix):
    blank_list = []
    for i in range(N):
        for j in range(M):
            if matrix[i][j] == 0:
                blank_list.append((i,j))
    return list(combinations(blank_list, 3))

def bfs(grid):
    cnt = 0
    dirs = [(1,0), (-1,0), (0,1), (0,-1)]
    queue = deque()
    for i in range(N):
        for j in range(M):
            if grid[i][j] == 2:
                queue.append((i, j))
    
    while queue:
        cx, cy = queue.popleft()
        for dx, dy in dirs:
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < N and 0 <= ny < M:
                if grid[nx][ny] == 0:
                    grid[nx][ny] = 2
                    queue.append((nx, ny))
    
    for i in range(N):
        for j in range(M):
            if grid[i][j] == 0:
                cnt += 1
    
    return N * M - cnt

def get_safe_area():
    max_dim = 0
    blanks = get_blank_list(grid)
    for blank in blanks:    # ((2, 6), (3, 2), (6, 2))
        for i in range(3):
            x, y = blank[i][0], blank[i][1]
            grid[x][y] == 1

        max_dim = max(max_dim, bfs(grid))
    print(max_dim)

N, M = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(N)]
get_safe_area()