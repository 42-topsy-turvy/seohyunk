# BOJ 12904 A와 B
import sys

S = sys.stdin.readline().strip()
T = sys.stdin.readline().strip()

# 문자열의 뒤에 A 추가 -> 문자열의 뒤에서 A 빼기
# 문자열을 뒤집고 뒤에 B 추가 -> 문자열의 맨 뒤에서 B 빼고 뒤집기

def reverse(str):
    return str[::-1]

def AB(S, T):
    # for i in range(len(T)):
    while len(T) > len(S):
        # print(1 if T==S else 0)
        # print("T ",T)
        # print("S ", S)
        # if T == S:
        #     return 1
        if T[-1] == 'A':
            T = T[:-1]
        elif T[-1] == 'B':
            T = T[:-1]
            T = reverse(T)
    return 1 if T == S else 0

print(AB(S, T))