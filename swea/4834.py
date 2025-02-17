# swea 4834 숫자카드

T = int(input())

for case in range(T):
    N = int(input())
    cards = [c for c in input()]
    max_item = max(cards,key=cards.count)
    print(f'#{case+1} {max_item} {cards.count(max_item)}')