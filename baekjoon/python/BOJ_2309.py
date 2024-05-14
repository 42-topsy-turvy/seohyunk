# BOJ 2309 일곱 난쟁이

import itertools

height = []
for i in range(9):
    height.append(int(input()))
height.sort(reverse=False)
combination = list(itertools.combinations(height, 7))

for i in range(len(combination)):
    if sum(combination[i]) == 100:
        for j in range(len(combination[i])):
            print(combination[i][j])
        break
