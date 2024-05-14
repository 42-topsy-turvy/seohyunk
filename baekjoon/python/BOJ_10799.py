# BOJ 10799 쇠막대기

import sys

batch = list(sys.stdin.readline().strip())

stack = []
stick_num = 0

for i in range(len(batch)):
    #print(i+": "+stack)
    if batch[i] == "(":
        stack.append(batch[i])
    else:
        if batch[i - 1] == "(":
            stack.pop()
            stick_num += len(stack)
        else:
            stack.pop()
            stick_num += 1

print(stick_num)

