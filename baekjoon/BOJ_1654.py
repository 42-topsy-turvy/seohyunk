# bOJ 1654 랜선 자르기

import sys
K, N = map(int, sys.stdin.readline().split())
lan_list = []
for i in range(K):
    lan_list.append(int(sys.stdin.readline().rstrip()))

start, end = 1, max(lan_list)
while start <= end:
    mid = (start + end) // 2
    lan_num = 0
    for lan in lan_list:
        lan_num += lan // mid
    
    if lan_num >= N:
        start = mid + 1
    else:   # lan_num < N
        end = mid - 1

print(end)