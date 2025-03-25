# BOJ 1010 다리놓기

from functools import reduce

def factorial_reduce(n):
    if n == 0: return 1
    return reduce(lambda x, y: x * y, range(1, n+1))
    

T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    print(factorial_reduce(M) // (factorial_reduce(N) * factorial_reduce(M-N)))