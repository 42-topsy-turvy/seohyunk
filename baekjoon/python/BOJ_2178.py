# BOJ 2178 미로 탐색

import sys
from collections import deque


# 최단거리 -> BFS
def BFS(graph, row, column):
    # visited = [[False for _ in range(column)] for _ in range(row)]
    # => True의 가능성이 여러개임 == 여러 방향이 가능할 수도 => 모조리 True로 됨
    visited = [[0 for _ in range(column)] for _ in range(row)]
    queue = deque()
    queue.append((0, 0)) # (1, 1)
    visited[0][0] = 1
    
    # graph[i][j] 기준
    # 우, 하, 좌, 상
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    while queue:
        current_i, current_j = queue.popleft()
        
        if current_i == row - 1 and current_j == column - 1:
            # break
            # return sum(sum(row) for row in visited)
            return visited[row - 1][column - 1]

        # 4방향, 범위 내, 조건에 맞으면 큐에 삽입
        for direct_i, direct_j in directions:
            next_i, next_j = current_i + direct_i, current_j + direct_j
            # 다음 좌표의 x값과 y값이 범위 내에 있고 / 다음 좌표 값이 1이고 / 방문을 안 한 곳이라면
            if 0 <= next_i < row and 0 <= next_j < column and graph[next_i][next_j] == 1 and not visited[next_i][next_j]:
                queue.append((next_i, next_j))
                visited[next_i][next_j] = visited[current_i][current_j] + 1
            # elif 0 <= di < row and 0 <= nj < column and graph[di][nj] == 1 and not visited[di][nj]:
            #     queue.append((di, nj))
            #     visited[di][nj] = True
    # print(visited)

    # return sum(sum(row) for row in visited)
    return visited[row - 1][column - 1]

def main():
    N, M = map(int, sys.stdin.readline().rstrip().split())
    # maze = []

    # for _ in range(N):
    #     maze.append(list(map(int, sys.stdin.readline().rstrip())))
    arr = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(N)]

    print(BFS(arr, N, M))


if __name__ == "__main__":
    main()