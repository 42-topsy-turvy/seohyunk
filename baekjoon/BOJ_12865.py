# BOJ 12865 평범한 배낭

import sys

# N: 물품 수
# K: 최대 무게
N, K = map(int, sys.stdin.readline().split())
dict = {}
dp = {}
for i in range(N):
    W, V = map(int, sys.stdin.readline().split())
    dict[W] = V

for i in range()