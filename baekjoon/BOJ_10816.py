# BOJ 10816 숫자 카드 2

from bisect import bisect_left, bisect

N = int(input())
cards = list(map(int, input().rstrip().split()))
M = int(input())
nums = list(map(int, input().rstrip().split()))

cards.sort()
result = []
def count_bi(nums, value):
    return bisect(nums, value) - bisect_left(nums, value)


for num in nums:
    result.append(count_bi(cards, num))
print(*result)