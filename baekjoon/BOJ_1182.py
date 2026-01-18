# BOJ 1182 부분수열의 합

import sys
input = sys.stdin.readline

N, S = map(int, input().split())
numbers = list(map(int, input().split()))

cnt = 0

def subset_sum(idx, sub_sum):
    global cnt
    
    if idx >= N:
        return
    
    sub_sum += numbers[idx]
    
    if sub_sum == S:
        cnt += 1
     
    subset_sum(idx + 1, sub_sum)
    subset_sum(idx + 1, sub_sum - numbers[idx])
    
subset_sum(0, 0)
print(cnt)
    


