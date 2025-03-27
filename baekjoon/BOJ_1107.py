# BOJ 1107 리모컨

import sys
import itertools

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())
broken_nums = list(map(int, sys.stdin.readline().split()))
num_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
listsss = []

if(M == 0):
    broken_nums = []
    print(len(str(N)))
elif(M == 10):
    print(abs(N - 100))
else:
    possible_nums = list(map(str, [i for i in num_list if i not in broken_nums]))
    channels = list(itertools.product(possible_nums, repeat = len(str(N))))
    for i in channels:
        listsss.append(abs(int(''.join(i)) - N))
    print(min(min(listsss) + len(str(N)), abs(N - 100)))

# result = abs(N-100)

# for tmp in range(1000001):
#     tmp = str(tmp)
#     for i in range(len(tmp)):
#         if(int(tmp[i]) in broken_nums):
#             break
#         else:
#             result = min(result, abs(int(tmp) - N) + len(tmp))

# print(result)