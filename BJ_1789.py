S = int(input())

num_list = []
i = 1
while S > 0:
    num_list.append(i)
    S = S - i
    i += 1
    if S == 0:
        break
    elif S <= i:
        num_list.append(S)
        break


cnt_last = num_list.count(num_list[-1])
if cnt_last == 2:
    for j in range(num_list[-1]):
        num_list[-j-1] += 1
    num_list.pop(-1)
print(len(num_list))