# BOJ 2864 5와 6의 차이

first, second = map(int, input().split())

first_list = list(map(int, str(first)))
second_list = list(map(int, str(second)))

min_first_list = list()
min_second_list = list()

max_first_list = list()
max_second_list = list()

for i, j in zip(range(len(first_list)), range(len(second_list))):
    if first_list[i] == 6:
        first_list[i] = 5
    if second_list[j] == 6:
        second_list[j] = 5
    min_first_list.append(first_list[i])
    min_second_list.append((second_list[i]))
first_s = [str(integer) for integer in min_first_list]
min_first = "".join(first_s)
min_first = int(min_first)
second_s = [str(integer) for integer in min_second_list]
min_second = "".join(second_s)
min_second = int(min_second)

for i, j in zip(range(len(first_list)), range(len(second_list))):
    if first_list[i] == 5:
        first_list[i] = 6
    if second_list[j] == 5:
        second_list[j] = 6
    max_first_list.append(first_list[i])
    max_second_list.append((second_list[i]))
first_s = [str(integer) for integer in max_first_list]
max_first = "".join(first_s)
max_first = int(max_first)
second_s = [str(integer) for integer in max_second_list]
max_second = "".join(second_s)
max_second = int(max_second)

print(min_first + min_second, end=" ")
print(max_first + max_second)