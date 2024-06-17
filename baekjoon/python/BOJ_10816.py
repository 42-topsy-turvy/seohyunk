# BOJ 10816 숫자 카드 2

from bisect import bisect_left, bisect

N = int(input())
cards = list(map(int, input().rstrip().split()))
M = int(input())
nums = list(map(int, input().rstrip().split()))

cards.sort()
result = []
def count_bi(nums, value):
    ri = bisect(nums, value)
    if ri != 0:
        return ri - bisect_left(nums, value)
    else:
        return 0;

for num in nums:
    result.append(count_bi(cards, num))
print(*result)