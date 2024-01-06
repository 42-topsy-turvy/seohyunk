# BOJ 26069 붙임성 좋은 총총이

N = int(input())

name_set = set(['ChongChong'])
for i in range(N):
    name_1, name_2 = input().split()

    if name_1 in name_set or name_2 in name_set:
        name_set.update([name_1, name_2])
    else:
        continue

print(len(name_set))

