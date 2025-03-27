# programmers 389479 서버 증설 횟수

from collections import deque
def solution(players, m, k):
    queue = deque()
    answer = 0
    for player in players:
        if queue:
            queue = deque(x - 1 for x in queue)
        while queue:
            if queue[0] == 0:
                queue.popleft()
            else:
                break
        if player >= (len(queue) + 1) * m:
            for i in range((player - (len(queue)+1) * m)//m + 1):
                queue.append(k)
                answer += 1
    return answer