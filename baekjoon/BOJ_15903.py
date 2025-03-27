# BOJ 15903 카드 합체 놀이

import os
import sys
import heapq

n, m = map(int, sys.stdin.readline().split())
cards = list(map(int, input().split()))
heapq.heapify(cards)
sum = 0

for i in range(m):
    x = heapq.heappop(cards)
    y = heapq.heappop(cards)

    heapq.heappush(cards, x + y)
    heapq.heappush(cards, x + y)

for i in range(len(cards)):
    sum += cards[i]

print(sum)