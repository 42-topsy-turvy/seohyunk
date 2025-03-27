# BOJ 9012 괄호

import sys

T = int(input())
isVPS = []
for i in range(T):
    stack = []
    VPS = input()
    for ch in VPS:
        if ch == "(":
            stack.append("(")
        elif ch == ")":
            if VPS:
                stack.pop()
            else:
                isVPS.append(False)
                break
    if isVPS == False:
        print("NO")
    else:
        print("YES")
