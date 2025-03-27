# BOJ 14940 쉬운 최단거리

import sys
from collections import deque

def BFS(row, col, map):
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    visited = [[False for j in range(col)] for i in range(row)]
    queue = deque([])
    result = [[-1 for j in range(col)] for i in range(row)]
    # start
    for i in range(row):
        for j in range(col):
            if map[i][j] == 0:
                result[i][j] = 0
            elif map[i][j] == 2:
                queue.append((i, j))
                visited[i][j] = True
                map[i][j] = 0
                result[i][j] = 0
            # elif map[i][j] == 0:
            #     result[i][j] == 0

    # print(result)
        
    
    # BFS
    while queue:
        i, j = queue.popleft()
        for di, dj in directions:
            # 빠진 부분
            ni, nj = i + di, j + dj
            #if not visited[ni][nj] and map[ni][nj] == 1 and 0 <= ni < row and 0 <= nj < col:
            if 0 <= ni < row and 0 <= nj < col and not visited[ni][nj] and map[ni][nj] == 1:
                queue.append((ni, nj))
                visited[ni][nj] = True
                result[ni][nj] = result[i][j] + 1
            # if 0 <= ni < row and 0 <= nj < col and not visited[ni][nj] and map[ni][nj] == 0:
            #     result[ni][nj] == 0
    for row in result:
        print(*row)


def main():
    N, M = map(int, sys.stdin.readline().split())

    arr = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]

    BFS(N, M, arr)
    

if __name__ == "__main__":
    main()