def Queue():

    queue = []
    queue.append()
    queue.pop()

    # 성능이 별로

from collections import deque

queue = deque([4, 5, 6])
queue.append(7)
queue.popleft() # 4
