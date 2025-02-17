# swea 11092 최대 최소의 간격

def interval_max_min():
    T = int(input())

    for case in range(T):
        N = int(input())
        nums = list(map(int, input().split()))

        # 반복문동안 최솟값/최댓값을 저장할 변수
        min_value, max_value = nums[0], nums[0]
        # 반복문동안 최소/최댓값의 인덱스를 저장할 변수
        min_idx, max_idx = 0, 0

        for j in range(len(nums)):
            # 최솟값) 같은 수가 존재할 경우, 가장 먼저 나오는 위치
            if nums[j] < min_value:     # '=' 없는 부등호를 이용해 같은 값이 나와도 갱신 X
                min_value, min_idx = nums[j], j

            # 최댓값) 같은 수가 존재할 경우, 가장 나중에 나오는 위치
            if nums[j] >= max_value:    # '>=' 부등호를 이용해 같은 값이 나오면 최댓값 갱신
                max_value, max_idx = nums[j], j

        # print(f'{min_idx} {max_idx}')

        # 절댓값 구하기
        # 1. if문 사용
        print(f'#{case + 1} {(max_idx - min_idx) if max_idx > min_idx else (min_idx - max_idx)}')
        # 2. abs() 사용
        print(f'#{case + 1} {abs(max_idx - min_idx)}')


if __name__ == '__main__':
    interval_max_min()
