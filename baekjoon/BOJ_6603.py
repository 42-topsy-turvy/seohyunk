# BOJ 6603 로또

import sys
input = sys.stdin.readline

def backtracking(depth, start):
    if depth == 6:
        print(*result)
        return
    
    for i in range(start, k):
        if visited[i]:
            continue
        
        visited[i] = True
        result.append(numbers[i])
        backtracking(depth+1, i + 1)
        result.pop()
        visited[i] = False
        
while True:
    k, *numbers = map(int, input().split())
    if k == 0:
        break
    numbers.sort()

    result = []
    visited = [False] * k
    backtracking(0, 0)
    print()