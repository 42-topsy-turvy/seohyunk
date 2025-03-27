# BOJ 10830 행렬 제롭

N, B = map(int, input().split())

matrix=[]
result=[]
for i in range(N):
    matrix[i] = tuple(map(int, input().split()))
    for j in range(B - 1):
        