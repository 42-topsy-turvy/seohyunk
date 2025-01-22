# BOJ 18870 좌표 압축
N = int(input())
num_list = list(map(int, input().split()))

use_list = sorted(set(num_list)).copy()
cnt_dict = dict()

for i in range(len(use_list)):
    cnt_dict[use_list[i]] = i

for i in num_list:
    print(cnt_dict[i], end= " ")
