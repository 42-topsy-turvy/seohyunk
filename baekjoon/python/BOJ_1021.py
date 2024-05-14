# BOJ 1021 : 회전하는 큐

from collections import deque

N, M = map(int, input().split())
nums = list(map(int, input().split()))
answer = 0

nums_queue = deque()
for i in range(N):
    nums_queue.append(i + 1)

for i in nums:
    while True:
        if i == nums_queue[0]:
            nums_queue.popleft()
            break
        elif nums_queue.index(i) <= len(nums_queue) // 2:
            nums_queue.rotate(-1)
            answer += 1
        else:
            nums_queue.rotate(1)
            answer += 1

print(answer)