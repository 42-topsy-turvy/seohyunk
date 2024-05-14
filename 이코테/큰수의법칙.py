N, M, K = map(int, input().split())

data = list(map(int, input().split()))

data.sort(reverse=True)

sum = 0

for i in range(M):
    for j in range(K):
        sum += data[0]
        if j == K-1:
            j = 0
            sum += data[1]

print(sum)