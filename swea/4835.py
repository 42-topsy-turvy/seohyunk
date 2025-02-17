# swea 4835 구간합

def block_sum():
    T = int(input())

    for case in range(T):
        N, M = map(int, input().split())
        nums = list(map(int, input().split()))
        sums = [0 for _ in range(N - M + 1)]
        '''
        왜 (N - M + 1)로 range를 잡아야 하는지?
        ->  N=10, M=3으로 가정했을 때,
            N-M=7 ->
        '''

        for i in range(N - M + 1):
            sums[i] = sum(nums[i:i + M])

        print(f'#{case + 1} {max(sums) - min(sums)}')


if __name__ == '__main__':
    block_sum()
