# BOJ 5430 AC

import sys
from collections import deque

T = int(sys.stdin.readline())

for i in range(T):
    p = sys.stdin.readline().rstrip()
    n = int(sys.stdin.readline())
    nums = deque(sys.stdin.readline().rstrip()[1:-1].split(","))

    # p = p.replace("RR", "")
    # print(p)
    if n == 0:
        nums = deque()
    
    flag = 0
    rev = 0
    for j in p:
        if j == "R":
            if (rev == 0):
                rev = 1
            elif (rev == 1):
                rev = 0
        elif (j == "D" and len(nums) != 0):
            if rev % 2 == 1:
                nums.pop()
            else:
                nums.popleft()
        else:
            print("error")
            flag = 1
            break

    if (flag == 0 and rev == 1):
        nums.reverse()
        print("[" + ",".join(nums) + "]")
    elif (flag == 0 and rev == 0):
        print("[" + ",".join(nums) + "]")

# reverse : O(n)
# R을 만날때마다 뒤집으면 100,000 * 100,000
# R이 짝수이면 안뒤집히는걸 사용