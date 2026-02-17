# BOJ 10819 차이를 최대로

import sys

input = sys.stdin.readline

N = int(input())
numbers = list(map(int, input().split()))
result = []
visited = [False] * N

def sum(list):
    length = len(list)
    val = 0
    for i in range(0, length - 1):
        val += abs(list[i] - list[i+1])
        
    return val

def backtracking(depth, cur):
    if depth == N:
        result.append(sum(cur))
        return
    
    for i in range(N):
        if not visited[i]:
            visited[i] = True
            cur.append(numbers[i])
            backtracking(depth + 1, cur)
            cur.pop()
            visited[i] = False


backtracking(0, [])
print(max(result))

