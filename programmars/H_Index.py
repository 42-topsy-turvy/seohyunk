# 프로그래머스 H-Index

def solution(citations):
    answer = 0
    citations.sort(reverse=True)
    for i in range(len(citations)):
        if (len(list(filter(lambda x: x >= citations[i], citations))) >= citations[i]):
            answer = citations[i]
        else:
            continue

    return answer

list_ = [3, 0, 6, 1, 5]
print(solution(list_))