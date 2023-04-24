n = 1
while 1:
    L, P, V = map(int, input().split())
    if L == 0 and P == 0 and V == 0:
        break
    elif L == 0 or P == 0 or V == 0:
        print(f'Case {n}:', 0)
    else:
        N = V // P
        DAY = N * L
        DAY = DAY + min(V % P, L)
        print(f'Case {n}:', DAY)
    n = n + 1

