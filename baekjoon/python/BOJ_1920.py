# BOJ 1920 수 찾기

import sys

N = int(sys.stdin.readline().rstrip())
A_arr = list(map(int, sys.stdin.readline().rstrip().split()))
M = int(sys.stdin.readline().rstrip())
nums = list(map(int, sys.stdin.readline().rstrip().split()))
A_arr.sort()
# result = []
for num in nums:
    start, end = 0, N - 1
    isExist = False

    while start <= end:
        mid = (start + end) // 2
        if num == A_arr[mid]:
            isExist = True
            print(1)
            break
        elif num > A_arr[mid]:
            start = mid + 1
        else:
            end = mid - 1
    
    if not isExist:
        print(0)