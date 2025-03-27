# BOJ 1138 한 줄로 서기

import sys

N = int(sys.stdin.readline())
list = list(map(int, sys.stdin.readline().split()))

ans_list = [0 for i in range(N)]

for i in range(N):
    # print("i= ",i)
    zero_cnt = 0
    for j in range(N):
        if zero_cnt == list[i] and ans_list[j] == 0:
            ans_list[j] = i + 1
            break
        elif ans_list[j] == 0:
            zero_cnt += 1
    # for j in range(N):
    #     print("j= ", j)
    #     if ans_list[j] == 0:
    #         zero_cnt += 1
    #     if zero_cnt == list[i]:
    #         if ans_list[j + 1] == 0:
    #             ans_list[j + 1] = i + 1
    #         else:
    #             continue
    #         break
print(*ans_list)