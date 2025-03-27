# BOJ 1747 서스 & 팰린드롬

import sys
import math

def is_Palindrome(n):
    n = str(n)
    length = len(n)
    for i in range(int(length/2)):
        if n[i] != n[length - 1 - i]:
            return False
        else:
            continue
    return True

N = int(sys.stdin.readline())

primes = []

max_prime = 1299709
era = [True for i in range(max_prime + 1)]
for i in range(2, int(math.sqrt(max_prime)) + 1):
    if era[i] == True:
        j = 2
        while i * j <= max_prime:
            era[i * j] = False
            j += 1

primes = [i for i, prime in enumerate(era) if prime and i>= 2]
palin_primes = []

for i in range(len(primes)):
    if is_Palindrome(primes[i]) == True:
        palin_primes.append(primes[i])

for i in range(len(palin_primes)):
    if N <= palin_primes[i]:
        answer = palin_primes[i]
        break
print(answer)