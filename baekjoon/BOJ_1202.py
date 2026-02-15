# BOJ 1202 보석 도둑
import heapq
import sys

input = sys.stdin.readline

N, K = map(int, input().split())

gems = []
for _ in range(N):
    M, V = map(int, input().split())
    gems.append((M, V))
    
gems.sort()

# print(gems)

bags = []
for _ in range(K):
    bags.append(int(input()))
    
bags.sort()
result = 0

heap = []
gem_idx = 0

for bag in bags:
    while gem_idx < N and gems[gem_idx][0] <= bag:
        heapq.heappush(heap, -gems[gem_idx][1])
        gem_idx += 1
    if heap:
        result += -heapq.heappop(heap)

print(result)