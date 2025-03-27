# BOJ 1446 지름길

import sys

N, D = map(int, sys.stdin.readline().split())

list = [list(map(int, input().split())) for _ in range(N)]
dis = [i for i in range(D + 1)]

# D =10
# dis = [0 1 2 3 4 5 6 7 8 9 10]

#print("list: ", list)
print("dis: ", dis)
# 50km 지점에서 20km
# 51km 지점에선 20Km + 1 / 51

for i in range(D + 1):
    if i > 0:
        dis[i] = min(dis[i], dis[i - 1] + 1)
    for start, end, distance in list:
        if i == start and end <= D and dis[i] + distance < dis[end]:
            dis[end] = dis[i] + distance
print(dis)
#print(dis[D])