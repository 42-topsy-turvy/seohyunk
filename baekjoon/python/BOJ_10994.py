# BOJ 10994 별 찍기 - 19

import sys

N = int(sys.stdin.readline())

stars = [[' ' for _ in range(4 * N - 3)]for _ in range(4 * N - 3)]

def recursive(k, stars):
    global N
    length = 4 * N - 3

    if N == 1:
        stars[0][0] = '*'
        return stars
    if k == N:
        return stars

    for i in range(length):
        stars[0][i] = '0'   # 첫 번째 줄
        stars[2 * k + 1][0] = '1'   # 홀수 행 첫번째 열
        stars[2 * k + 1][-1] = '2'  # 홀수 행 마지막 열
        stars[length - 1][i] = '3'  # 마지막 줄
        stars[2 * k + 2][0] = '4'
        stars[2 * k + 2][-1] = '5'

    recursive(k + 1, stars)

    return stars

recursive(0, stars)

for i in stars:
    for j in i:
        print(j, end='')
    print()