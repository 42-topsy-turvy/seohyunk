A, B, C, M = map(int, input().split())

'''
A : 한 시간 일했을 때 쌓이는 피로도
B : 한 시간 일했을 때 처리할 수 있는 일의 양
C : 한 시간 일했을 떄 줄어드는 피로도
M : 하루 최대 피로도 -> 넘기면 안됨.

피로도는 0보다 작아질 수 없다.
'''
working = 0
tired = 0

for i in range(24):
    if A > M:
        break
    if tired + A <= M:  # 왜 tired < M
        tired += A
        working += B
    elif tired + A > M:     # tired >= M 으로 했을 때 안되냐
        tired -= C
        working += 0
        if tired <= 0:
            tired = 0
print(working)