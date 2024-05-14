# BOJ 10773 제로

K = int(input())

stack = []
for i in range(K):
    price = int(input())
    if price == 0:
        stack.pop()
    else:
        stack.append(price)

print(sum(stack))