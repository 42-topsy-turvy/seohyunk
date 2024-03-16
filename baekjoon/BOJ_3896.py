# BOJ 3896 소수 사이 수열
import sys
import math

def binary_search(arr, k):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == k:
            return mid, mid  # k가 소수인 경우
        elif arr[mid] < k:
            left = mid + 1
        else:
            right = mid - 1
    return right, left

T = int(sys.stdin.readline())
answer = []
primes = []

max_prime = 1299709
era = [True for i in range(max_prime + 1)]
for i in range(2, int(math.sqrt(max_prime)) + 1):
    if era[i] == True:
        j = 2
        while i * j <= max_prime:
            era[i * j] = False
            j += 1
for i in range(2, max_prime + 1):
    if era[i]:
        primes.append(i)
# primes = [i for i, prime in enumerate(era) if prime and i>= 2]

# 전체 탐색 -> 시간 초과
# for i in range(T):
#     k = int(sys.stdin.readline())
#     if k in primes:
#         answer.append(0)
#     else:
#         for j in range(len(primes)):
#             if k < primes[j]:
#                 answer.append(primes[j] - primes[j - 1])
#                 break
        
# 이진 탐색
for _ in range(T):
    k = int(sys.stdin.readline())
    if k in primes:
        answer.append(0)
    else:
        left_idx, right_idx = binary_search(primes, k)
        answer.append(primes[right_idx] - primes[left_idx])

for ans in answer:
    print(ans)