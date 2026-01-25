# BOJ 15656 N과 M(7)

import sys
input = sys.stdin.readline

N, M = map(int, input().split())
numbers = list(map(int, input().split()))
numbers.sort()

result = []

def backtracking(depth):
    if depth == M:
        print(*result)
        return
    
    for i in range(N):
        result.append(numbers[i])
        backtracking(depth + 1)
        result.pop()
        
backtracking(0)