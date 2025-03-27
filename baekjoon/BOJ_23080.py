K = int(input())
password = input()

for i in range(0, len(password), K):
    print(password[i], end="")