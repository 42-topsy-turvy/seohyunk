import math
def solution(progresses, speeds):
    workdays=[]
    for progress, speed in zip(progresses, speeds):
        workdays.append(math.ceil((100-progress)/speed))
    print(workdays)
    answer = []
    maxday=workdays[0]
    tasks=1
    for i in range(1, len(workdays)):
        if workdays[i] > maxday:
            answer.append(tasks)
            tasks=1
        else:
            tasks+=1
        maxday=max(maxday, workdays[i])
    answer.append(tasks)
    return answer