# BOJ 15666 N과 M(12)

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
numbers = list(map(int, input().split()))

numbers.sort()
result = []
all = set()

def backtracking(depth, start):
    if depth == M:
        if tuple(result) not in all:
            print(*result)
            all.add(tuple(result))
        return
    
    for i in range(start, N):
        result.append(numbers[i])
        backtracking(depth + 1, i)
        result.pop()
        
backtracking(0, 0)