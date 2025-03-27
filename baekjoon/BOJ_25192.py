# BOJ 25192 인사성 밝은 곰곰이

import sys
N = int(sys.stdin.readline())
chat_set = set([])
cnt = 0

for i in range(N):
    chat = sys.stdin.readline()
    if chat.strip() != "ENTER":
        chat_set.add(chat)
    else:
        cnt = cnt + len(chat_set)
        chat_set = set([])
cnt = cnt + len(chat_set)

print(cnt)

'''
N = int(input())
chat_set = set([])
cnt = 0

for i in range(N):
    chat = input()
    if chat != "ENTER":
        chat_set.add(chat)
    else:
        cnt = cnt + len(chat_set)
        chat_set = set([])
cnt = cnt + len(chat_set)

print(cnt)
'''