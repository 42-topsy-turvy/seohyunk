import sys
import math

N, K = map(int, sys.stdin.readline().split())
grades = list(map(int, sys.stdin.readline().split()))
average_grade = []
for i in range(K):
    sum_grade = 0
    first_step, second_step = map(int, sys.stdin.readline().split())
    for j in range(first_step - 1, second_step):
        sum_grade += grades[j]
    average_grade.append(f"{sum_grade / (second_step - first_step + 1):.2f}")

print(*average_grade, sep='\n')