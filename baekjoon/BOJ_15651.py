# BOJ 15651 N과 M(3)

import sys
input = sys.stdin.readline

N, M = map(int, input().split())

result = []

def backtracking(depth):
    if depth == M:
        print(*result)
        return
    
    for i in range(1, N+1):
        
        result.append(i)
        backtracking(depth + 1)
        result.pop()
        
backtracking(0)