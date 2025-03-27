# BOJ 14888 연산자 끼워넣기

import sys
import math

N = int(sys.stdin.readline())
nums_list = list(map(int, sys.stdin.readline().split()))
add, minus, multiple, div = map(int, sys.stdin.readline().split())

# 백트래킹 이용 위해 max min 설정
max_val = 1e+10
min_val = -1e+10
# 연산자 경우의 수
# ex) +, -, x, / -> 2, 1, 2, 0   => 총 5개
# 경우의 수는 5!/(2!2!)
# opers_nums = math.factorial(N - 1)/(math.factorial(oper_list[0]) * math.factorial(oper_list[1]) * math.factorial(oper_list[2]) * math.factorial(oper_list[3]))

def back_tracking(i, arr):
    global add, minus, multiple, div, max_val, min_val

    # i -> 현재까지 연산한 개수
    if i == N:
        max_val = max(answer, max_val)
        min_val = min(answer, min_val)
    
    else:
        if add > 0:
            answer = a + b
            add -= 1

back_tracking()

# i = N + 1
# 최대 최소 비교
# ㅑ < N -> 연산 뒤로 보내고
# i == N -> 연산 후 값 비교
