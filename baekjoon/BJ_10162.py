T = int(input())

time_list = [300, 60, 10]
click_list = list()

for i in time_list:
    click_list.append(int(T / i))
    T = T % i

if T != 0:
    print(-1)
else:
    for i in click_list:
        print(i, end=' ')
