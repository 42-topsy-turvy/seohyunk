# BOJ 11000 강의실 배정

import sys
import heapq

N = int(sys.stdin.readline())
time = []
room = []

for i in range(N):
    time.append(list(map(int, sys.stdin.readline().split())))

time.sort(key=lambda x:x[0])

# n + 1번째 시작 시간이 n번째 종료 시간보다 빨리 시작할때 == time[n][0] < room[i]
# 강의실 추가 배정
# 추가 배정 == 우선순위 큐에 n + 1 번째 시작 시간 heappush

heapq.heappush(room, time[0][1])
for i in range(1, N):
    if time[i][0] < room[0]:
        heapq.heappush(room, time[i][1])
    else:
        heapq.heappop(room)
        heapq.heappush(room, time[i][1])

print(len(room))