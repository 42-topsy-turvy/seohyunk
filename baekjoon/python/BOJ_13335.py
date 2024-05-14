# BOJ 13335 트럭

# 왜 예제1의 답이 7초가 아닌 8초인가?
# 트럭  1단위   2단위
#  7    1초    2초
#  4    3초
# 4+5       4초
#  5           5초
#  6    6초    7초      => 아직 다리 위에 버스가 존재
# 무게가 6인 트럭 빠지는 시간 + 1초

import sys
from collections import deque

n, w, L = map(int, sys.stdin.readline().split())
trucks = list(map(int, sys.stdin.readline().split()))

bridge = deque([])
for i in range(n):
    