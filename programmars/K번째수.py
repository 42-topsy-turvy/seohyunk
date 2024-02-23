# Programmars K번째 수
# 정렬

def solution(array, commands):
    answer = []
    for i in range(len(commands)):
        split_array = array[commands[i][0] - 1:commands[i][1]]
        split_array.sort()
        answer.append(split_array[commands[i][2] - 1])
    return answer