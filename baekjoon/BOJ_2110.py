# BOJ 2110 공유기 설치

N, C = map(int, input().split())
homes = []
for _ in range(N):
    homes.append(int(input()))
homes.sort()
start, end = 1, homes[-1] - homes[0]
answer = 0

while (start <= end):
    mid = (start + end) // 2
    current, count = homes[0], 1
    
    for i in range(1, N):
        if homes[i] >= current + mid:
            current = homes[i]
            count += 1
    if count >= C:
        start = mid + 1
        answer = mid
    else:
        end = mid - 1
        
print(answer)
