# BOJ 2447 별 찍기 - 10

import sys

N = int(sys.stdin.readline())
arr = [['*'] * N for _ in range(N)]

def recursive(k):
    