# swea 1206 View

for case in range(3):
    N = int(input())
    buildings = list(map(int, input().split()))
    fresh_house = 0
    for i in range(2, N-2):
        left_max = max(buildings[i-2], buildings[i-1])
        # print('left: ', left_max)
        right_max = max(buildings[i+2], buildings[i+1])
        # print('right: ', right_max)
        total_max = max(left_max, right_max)
        if buildings[i] > total_max:
            fresh_house += buildings[i] - total_max
            # print(i)
            # print(fresh_house)
    print(f'#{case+1} {fresh_house}')