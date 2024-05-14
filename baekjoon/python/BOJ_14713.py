# BOJ 14713 앵무새

from collections import deque

bird_count = int(input())
bird_sentence_list = list()

for i in range(bird_count):
    bird_sentence_list.append(deque(map(str, input().split())))
sentence = deque(map(str, input().split()))

def possible(sentence, arr):
    misscount = 0
    j = 0
    while sentence:
        if arr[j] and sentence[0] == arr[j][0]:
            arr[j].popleft()
            sentence.popleft()
            misscount = 0 
        else:
            if misscount == bird_count:
                return False
            misscount += 1 
        j = (j + 1) % bird_count

    empty = 0
    for i in range(bird_count):
        if len(arr[i]) == 0:
            empty += 1

    if not sentence and empty == bird_count: 
        return True
    else:
        return False

if possible(sentence, bird_sentence_list):
    print("Possible")
else:
    print("Impossible")
