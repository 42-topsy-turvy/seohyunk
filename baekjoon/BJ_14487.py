n = int(input())
v_list = list(map(int, input().split()))

v_list.sort()
v_list.pop(n-1)
cost = 0
for i in v_list:
    cost += i

print(cost)