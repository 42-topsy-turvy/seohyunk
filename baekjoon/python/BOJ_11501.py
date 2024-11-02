# BOJ 11501 주식

import sys

T = int(sys.stdin.readline())
while (T > 0):
    N = int(sys.stdin.readline())
    prices = list(map(int, sys.stdin.readline().split()))

    profit = 0  # 이익
    max_price = 0

    for i in range(len(prices)-1, -1, -1):
        max_price = max(max_price, prices[i])
        if(max_price >= prices[i]):
            profit += max_price - prices[i]
    
    print(profit)
    T -= 1