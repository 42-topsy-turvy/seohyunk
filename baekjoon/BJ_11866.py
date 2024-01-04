# BOJ 11866 요세푸스 문제 0

from collections import deque
N, K = map(int, input().split())

people_queue = deque()
answer_list = []
for i in range(N):
    people_queue.append(i+1)

while people_queue:
    people_queue.rotate(-(K-1))
    answer_list.append(people_queue.popleft())

print("<", end="")
for i in range(N-1):
    print(answer_list[i], end=", ")
print(answer_list[N-1], end="")
print(">")