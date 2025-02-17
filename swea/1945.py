# swea 1945 간단한 소인수분해

def simple_prime_factor():
    T = int(input())
    primes = [2, 3, 5, 7, 11]

    for t in range(T):
        N = int(input())
        counts = [0] * 5  # 인수의 개수를 저장할 리스트. 매 테케마다 초기화 필ㅇ
        # primes 리스트와 같은 인덱스 공유

        while N > 1:
            for idx, prime in enumerate(primes):  # primes의 인덱스를 함께 사용해서 counts에 저장
                while N % prime == 0:  # N이 해당 prime으로 나눠떨어지는 동안
                    N = N // prime  # '/' 나눗셈 기호는 float를 반환하므로, 정수 반환하는 '//' 사용
                    # print(N)
                    counts[idx] += 1  # 인수 리스트 1 증가

        # print(counts)
        print(f'#{t + 1} {counts[0]} {counts[1]} {counts[2]} {counts[3]} {counts[4]}')


if __name__ == '__main__':
    simple_prime_factor()
