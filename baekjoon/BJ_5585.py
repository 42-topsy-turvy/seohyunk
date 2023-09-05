M = int(input())
C = 1000 - M

change_list = [500, 100, 50, 10, 5, 1]

cnt = 0
for i in change_list:
    cnt += int(C / i)
    C = C % i
print(cnt)

'''안 나눠떨어질때 고려 안해도 되는지? 라기엔 1엔이 있구나'''