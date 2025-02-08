# BOJ 1012 유기농 배추

from collections import deque

class OrganicCabbage:
    def __init__(self, M, N, K, positions):
        self.M=M
        self.N=N
        self.matrix = [[0 for _ in range(M)]for _ in range(N)]

        for a, b in positions:
            self.matrix[b][a] = 1

    def bfs(self, a, b):
        dx = [0, 0, -1, 1]
        dy = [1, -1, 0, 0]

        queue = deque()
        queue.append((a,b))
        self.matrix[a][b] = 0
            
        while queue:
            x, y = queue.popleft()
            for idx in range(4):
                nx, ny = x + dx[idx], y + dy[idx]
                if 0 <= nx < self.N and 0 <= ny < self.M and self.matrix[nx][ny] == 1:
                    self.matrix[nx][ny] = 0
                    queue.append((nx, ny))
    
    def count_worms(self):
        worms = 0
        for i in range(self.N):
            for j in range(self.M):
                if self.matrix[i][j] == 1:
                    self.bfs(i, j)
                    worms += 1
        return worms

T = int(input())

for _ in range(T):
    M, N, K = map(int, input().split())
    positions = [tuple(map(int, input().split())) for _ in range(K)]
    farm = OrganicCabbage(M, N, K, positions)
                        
    print(farm.count_worms())




