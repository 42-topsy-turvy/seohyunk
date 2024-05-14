# BOJ 2164 카드2

from collections import deque

deque = deque()
N = int(input())

for i in range(N):
    deque.append(i+1)

while(len(deque)>1):
    deque.popleft()
    deque.rotate(-1)

print(deque[0])