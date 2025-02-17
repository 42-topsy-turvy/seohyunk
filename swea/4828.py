# swea 4828 min max

T = int(input())

for case in range(T):
    N = int(input())
    nums = list(map(int, input().split()))
    max_value, min_value = nums[0], nums[0]
    for num in nums:
        if num > max_value:
            max_value = num
        if num < min_value:
            min_value = num

    print(f'#{case+1} {max_value-min_value}')