# BOJ 13335 트럭
from collections import deque
n, w, L = map(int, input().split())     # 트럭 개수, 다리 길이, 최대 하중
trucks = deque(map(int, input().split()))

queue = deque()
