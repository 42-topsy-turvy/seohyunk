# swea 9386 연속한 1의 개수

def continuous_one_count():
    T = int(input())

    for t in range(T):
        N = int(input())
        nums = input()
        cnt, max_cnt = 0, 0     # 1을 만나면 증가시킬 변수, 최댓값을 갱신할 변수

        for i in range(len(nums)):
            if nums[i] == '1':   # 1을 만났을 때,
                cnt += 1    # cnt를 증가시켜 몇 개가 연속중인지 저장
                max_cnt = max(max_cnt, cnt)     # 지금까지의 연속 개수가 최댓값인지 확인 후 갱신 or 기존 값 유지
            else:
                cnt = 0     # 0을 만난 경우엔 측정 중이던 연속 개수 0으로 할당

        print(f'#{t + 1} {max_cnt}')


if __name__ == '__main__':
    continuous_one_count()
