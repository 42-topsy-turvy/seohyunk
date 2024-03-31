# BOJ 5397 키로커
import sys

# 백스페이스: -
# 화살표: <>

N = int(sys.stdin.readline())

for i in range(N):
    password = list(sys.stdin.readline().strip())

    left = []
    right = []

    for j in range(len(password)):
        if password[j] == "<":
            if left:
                right.append(left.pop())
            else:
                continue
        elif password[j] == ">":
            if right:
                left.append(right.pop())
            else:
                continue
        elif password[j] == "-":
            if left:
                left.pop()
            else:
                continue
        else:
            left.append(password[j])
    
    if right:
        right.reverse()
    print(left)
    print(right)
    print(*(left + right), sep="")