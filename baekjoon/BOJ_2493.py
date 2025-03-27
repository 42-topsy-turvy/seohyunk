# BOJ 2493 탑

N = int(input())
tops = list(map(int, input().split()))
length = len(tops)
result = [0 for _ in range(length)]

reverse_tops = tops[::-1]


# for i in range(length-1, 0, -1):
#     origin = tops.pop()
#     j = i - 1
#     while True:
#         if j == 0:
#             result[j] = 0
#             break
#         if tops[j] < origin:
#             j -= 1
#             continue
#         elif tops[j] >= origin:
#             result[i] = j + 1
#             break


print(*result)    
