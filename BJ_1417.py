'''국회의원 선거'''

N = int(input())
dasom = int(input())
vote = []
competitor = []
ans = 0

if N == 1:
    ans = 0
else:
    for _ in range(N - 1):
        vote.append(int(input()))

    for i in vote:
        if dasom > i:
            continue
        else:
            competitor.append(i)

    competitor = sorted(competitor, reverse=True)
    new_dasom = dasom

    while True:
        for i in competitor:
            if new_dasom <= i:
                new_dasom += 1
                i -= 1
                competitor[i] = i
        if competitor[0] < new_dasom:
            break
    ans = new_dasom - dasom
print(ans)