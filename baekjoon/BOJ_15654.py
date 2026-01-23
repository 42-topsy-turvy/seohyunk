# BOJ 15654 N과 M(5)

N, M = map(int, input().split())
numbers = list(map(int, input().split()))
numbers.sort()

result = []
visited = [False] * N

def backtracking(depth):
    if depth == M:
        print(*result)
        return
    
    for i in range(N):
        if visited[i]:
            continue
        
        visited[i] = True
        result.append(numbers[i])
        backtracking(depth + 1)
        visited[i] = False
        result.pop()

backtracking(0)