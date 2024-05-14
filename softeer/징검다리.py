import sys

N = int(sys.stdin.readline())
rock_list = list(map(int, sys.stdin.readline().split()))
answer = 0

# 높이 같은 건?

# 최대 길이를 구하는 것이므로 첫 번째 돌부터 시작할 필요 없다.
# for i in range(1, N):
#     if rock_list[i] >= real_rock[-1]:
#         real_rock.append(rock_list[i])

for i in range(N - 1):
    print("i:" , i)
    real_rock = [rock_list[i]]
    for j in range(i + 1, N):
        print("j: ", j)
        if rock_list[j] >= real_rock[-1]:
            real_rock.append(rock_list[j])
    k = len(real_rock)
    answer = max(answer, k)

print(answer)
    