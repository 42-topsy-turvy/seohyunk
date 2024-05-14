# BOJ 1107 리모컨

import sys

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

# # 현재 채널 100번
# N_list = [eval(i) for i in list(str(N))]
# current = 100

# while(current != N):

if(M == 0):
    broken_nums = []
else:
    broken_nums = list(map(int, sys.stdin.readline().split()))

result = abs(N-100)

for tmp in range(1000001):
    tmp = str(tmp)
    for i in range(len(tmp)):
        if(int(tmp[i]) in broken_nums):
            break
        else:
            result = min(result, abs(int(tmp) - N) + len(tmp))

print(result)

# 5000000
# broke_nums = [4, 9]