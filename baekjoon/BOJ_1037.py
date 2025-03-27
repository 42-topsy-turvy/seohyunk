# BOJ 1037 약수

cnt = int(input())
divisor = list(map(int, input().split()))

print(max(divisor)*min(divisor))