T = int(input())

unit_list = [25, 10, 5, 1]
for i in range(T):
    change = int(input())
    for j in unit_list:
        print(int(change / j), end=' ')
        change = change % j