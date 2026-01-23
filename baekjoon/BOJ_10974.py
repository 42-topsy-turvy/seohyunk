# BOJ 10974 모든 순열

import sys
input = sys.stdin.readline

N = int(input())
visited = [False] * (N + 1)
result = []

def backtracking(depth):
    if depth == N:
        print(*result)
        return
    
    for i in range(1, N + 1):
        if visited[i]:
            continue
        
        visited[i] = True
        result.append(i)
        backtracking(depth + 1)
        visited[i] = False
        result.pop()
        
backtracking(0)
        
    # if 종료조건:    
    #     결과처리
    #     return
    
    # for 선택 in 선택지:
    #     if 조건 위반:
    #         continue
        
    #     선택
    #     backtracking(다음 상태)
    #     원복