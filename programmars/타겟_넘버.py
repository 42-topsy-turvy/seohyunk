# programmers 타겟 넘버
def solution(numbers, target):
    answer = 0
    for i in range(len(numbers)):
        sum = numbers[i]
        for j in range(len(numbers)-1):
            sum = sum + numbers[j + 1]
            if sum > target:
                sum = sum - 2 * numbers[j + 1]
            elif sum < target:
                continue
            elif (sum == target) and (j == len(numbers) - 3):
                answer = answer + 1
                break

    return answer

