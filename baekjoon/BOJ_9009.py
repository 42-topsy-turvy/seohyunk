# BOJ 9009 피보나치

import sys
T = int(sys.stdin.readline())
fibo = [0, 1]
answer = [[]for i in range(T)]

for i in range(T):
    # print(i)
    N = int(sys.stdin.readline())
    while(N != 0):
        if(N > fibo[-1]):
            fibo.append(fibo[-1] + fibo[-2])
            #print(fibo)
        else:
            # for j in range(len(fibo) - 1):
            #     if N >= fibo[j] and N < fibo[j+1]:
            #         answer[i].append(fibo[j])
            #         # print(answer)
            #         N -= fibo[j]
            for num in reversed(fibo):
                if num <= N:
                    answer[i].append(num)
                    N -= num

for i in range(T):
    print(*sorted(answer[i][:-1]))