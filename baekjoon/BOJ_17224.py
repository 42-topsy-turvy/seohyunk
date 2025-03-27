N, L, K = map(int, input().split())
P = 1

score = 0
count = 0
while P <= N:
    sub1, sub2 = map(int, input().split())
    P = P + 1
    if (sub1 <= L) and (sub2 <= L):
        score = score + 140
        count = count + 1
    elif (sub1 <= L) and (sub2 > L):
        score = score + 100
        count = count + 1
    elif (sub1 > L) and (sub2 > L):
        score = score
        count = count
    if count == K:
        break

print(score)
#max로 어떻게 뽑는지