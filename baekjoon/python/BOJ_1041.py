'''
주사위
N과 주사위에 쓰여 있는 수가 주어질 때, 보이는 5개의 면에 쓰여 있는 수의 합의 최솟값을 출력하는 프로그램을 작성하시오.
'''
N = int(input())

A, B, C, D, E, F = map(int, input().split())

three_spaces = [A+C+E, A+B+F, A+B+D, A+D+E, B+D+F, B+C+F, C+E+F, D+E+F]
print(three_spaces)
two_spaces = [A+B, A+C, A+D, A+E, B+C, B+D, B+F, C+E, C+F, D+E, D+F, E+F]
print(two_spaces)
one_spaces = [A, B, C, D, E, F]
print(one_spaces)

three_min = min(three_spaces)
print(three_min)
two_min = min(two_spaces)
print(two_min)
one_min = min(one_spaces)
print(one_min)

three_sum = three_min * 8

two_sum = (N-2) * 12 * two_min
one_sum = (N-2) * (N-2) * 6 * one_min

sum = one_sum + two_sum + three_sum

print(sum)