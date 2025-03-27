# BOJ 16401 과자 나눠주기

# M명의 조카, N개의 과자
# 조카 1명에게 줄 수 있는 최대 길이
# 모두에게 같은 과자 길이

M, N = map(int, input().split())

snack_len = list(map(int, input().split()))

if M <= N:
    max_len = sorted(snack_len)[-M]
    print(max_len)
else:
    