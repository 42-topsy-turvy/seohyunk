# BOJ 1038 감소하는 수

import sys
input = sys.stdin.readline

N = int(input())

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
result = []

def backtracking(last_num, current_num):
    print(current_num)
    result.append(current_num)
    
    for next_digit in range(0, last_num):
        backtracking(next_digit, current_num * 10 + next_digit)
        
for start in range(10):
    backtracking(start, start)
    
result.sort()

if N >= len(result):
    print(-1)
else:
    print(result[N])
    