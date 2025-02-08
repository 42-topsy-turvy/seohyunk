# BOJ 2583 영역 구하기
from collections import deque
class getArea:
    def __init__(self, M, N, positions):
        self.M=M    # 행
        self.N=N    # 열
        self.matrix = [[0 for _ in range(M)]for _ in range(N)]

        for x1, y1, x2, y2 in positions:
            for i in range(x1, x2):  # 세로 범위 (행)
                for j in range(y1, y2):  # 가로 범위 (열)
                    self.matrix[i][j] = 1  # 해당 영역을 1로 채운다
    
    def bfs(self, a, b):
        area = 1
        queue = deque()
        queue.append((a, b))
        self.matrix[a][b] = 1

        dx = [0, 0, 1, -1]
        dy = [1, -1, 0, 0]

        while queue:
            x, y = queue.popleft()
            for dir_x, dir_y in zip(dx, dy):
                nx, ny = x + dir_x, y + dir_y
                if 0 <= nx < self.N and 0 <= ny < self.M and self.matrix[nx][ny]==0:
                    area += 1
                    # blank.append(area)
                    self.matrix[nx][ny] = 1
                    queue.append((nx, ny))
        return area

    def count_blank(self):
        areas = []
        for i in range(self.N):
            for j in range(self.M):
                if self.matrix[i][j]==0:
                    areas.append(self.bfs(i, j))
    
        areas.sort()
        print(len(areas))
        print(*areas)
        

M, N, K = map(int, input().split()) # M: 행, N: 열
positions = [tuple(map(int, input().split())) for _ in range(K)]

box = getArea(M, N, positions)
box.count_blank()