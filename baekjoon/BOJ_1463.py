# BOJ 1463 1로 만들기

import sys
N = int(sys.stdin.readline())

dp = [0] * (N + 1)  # N = 1, N = 2, N = 3, ...

# dp = [0] * (N+1)

def recursive(N):
    if N == 1:
        dp[N] = 0
        return dp[N]
    if N == 2 or N == 3:
        dp[N] = 1
        return dp[N]
    if dp[N] != 0:
        return dp[N]
    if (N % 2 == 0) and (N % 3 == 0):
        dp[N] = min(recursive(N // 2) + 1, recursive(N // 3) + 1)
    elif (N % 2 == 0):
        dp[N] = min(recursive(N // 2) + 1, recursive(N - 1) + 1)
    elif (N % 3 == 0):
        dp[N] = min(recursive(N // 3) + 1, recursive(N - 1) + 1)

    else:
        dp[N] = recursive(N - 1) + 1

    return dp[N]

print(recursive(N))

# def recursive(N):
#     if N == 1:
#         dp[N - 1] = 0
#         return dp[N - 1]
#     if N == 2 or N == 3:
#         dp[N - 1] = 1
#         return dp[N - 1]
#
#     if (N % 2 == 0) and (N % 3 == 0):
#         if (dp[N // 2 - 1] != 0) and (dp[N // 3 - 1] != 0):
#             dp[N - 1] = min(dp[N // 2 - 1] + 1, dp[N // 3 - 1] + 1)
#         elif dp[N // 2 - 1] != 0:
#             dp[N - 1] = min(dp[N // 2 - 1] + 1, recursive(N // 3) + 1)   # N = 12 같은 경우, 2와 3 모두로 나눠짐 -> 2로 나눴을 때의 횟수와 3으로 나눴을 때의 횟수 중 최솟값
#         elif dp[N // 3 - 1] != 0:
#             dp[N - 1] = min(dp[N // 3] + 1, recursive(N // 2) + 1)
#         else:
#             dp[N - 1] = min(recursive(N // 2) + 1, recursive(N // 3) + 1)
#
#     elif (N % 2 == 0):
#         if (dp[N // 2 - 1] != 0) and (dp[N - 2] != 0):
#             dp[N - 1] = min(dp[N // 2 - 1] + 1, dp[N - 2] + 1)
#         elif dp[N // 2 - 1] != 0:
#             dp[N - 1] = min(dp[N // 2 - 1] + 1, recursive(N - 1) + 1)
#         elif dp[N - 2] != 0:
#             dp[N - 1] = min(recursive(N // 2) + 1, dp[N - 2] + 1)
#         else:
#             dp[N - 1] = min(recursive(N // 2) + 1, recursive(N - 1) + 1)
#
#     elif (N % 3 == 0):
#         if (dp[N // 3 - 1] != 0) and (dp[N - 2] != 0):
#             dp[N - 1] = min(dp[N // 3 - 1] + 1, dp[N - 2] + 1)
#         elif dp[N // 3 - 1] != 0:
#             dp[N - 1] = min(dp[N // 3 - 1] + 1, recursive(N - 1) + 1)
#         elif dp[N - 2] != 0:
#             dp[N - 1] = min(recursive(N // 3) + 1, dp[N - 2] + 1)
#         else:
#             dp[N - 1] = min(recursive(N // 3) + 1, recursive(N - 1) + 1)
#
#
# => 시간초과

