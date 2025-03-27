# BOJ 1406 에디터

import sys
from collections import deque
left = list(input())
right = []
N = int(input())

for i in range(N):
    command = list(sys.stdin.readline().split())
    if command[0] == "L" and left:
        right.append(left.pop())
    elif command[0] == "D" and right:
        left.append(right.pop())
    elif command[0] =="B" and left:
        left.pop()
    elif command[0] == "P":
        left.append(command[1])

if right:
    right.reverse()

print(*(left+right), sep="")
#print(*right, sep="")