def solution(participant, completion):
    answer = ''
    participant.sort()
    completion.sort()
    # print(participant)
    # print(completion)
    for i in range(len(participant)):
        if i == len(participant) - 1:
            return participant[-1]
        elif participant[i] != completion[i]:
            return participant[i]
