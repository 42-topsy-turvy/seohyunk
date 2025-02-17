# swea 6485 삼성시의 버스 노선
def samsung_bus_route():
    T = int(input())

    for tc in range(T):
        N = int(input())

        # 각 버스가 다니는 정류장 입력 위한 N * 2 크기의 이차원 배열
        buses = []

        for i in range(N):  # N개의 버스 종점 입력 - A/B
            A, B = map(int, input().split())
            buses.append((A, B))
        P = int(input())
        stop_buses = [0 for _ in range(P)]  # 정류장에 정차하는 버스 개수 저장 위한 배열

        for i in range(P):  # 각 정류장마다 몇 개의 버스가 정차하는지 검사하는 반복문
            stop_num = int(input())  # 검사할 정류장 번호 입력
            for j in range(N):  # 버스 별 해당 정류장에 정차하는지 검사하는 반복문
                if buses[j][0] <= stop_num <= buses[j][1]:  # 해당 버스가 다니는 경로에 정류장 존재하는지 확인
                    stop_buses[i] += 1

        print(f'#{tc + 1} {" ".join(map(str, stop_buses))}')


if __name__ == '__main__':
    samsung_bus_route()
