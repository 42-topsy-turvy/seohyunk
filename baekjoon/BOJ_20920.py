# BOJ 20920 영단어 암기는 괴로워

import sys

N, M = map(int, sys.stdin.readline().split())

# N: 단어 개수
# M: 단어 길이

# 1. 자주 나오는 단어
# 2. 단어의 길이가 길수록
# 3. 사전 순

words = []
for _ in range(N):
    word = sys.stdin.readline().rstrip()

    if len(word) < M:
        continue
    else:
        words.append(word)




print(words)