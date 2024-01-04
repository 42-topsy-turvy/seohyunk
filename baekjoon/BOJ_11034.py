# BOJ 11034 컁고류 

while 1:
    try:
        loc_a, loc_b, loc_c = map(int, input().split())
        print(max((loc_b - loc_a), (loc_c - loc_b)) - 1)
    except:
        break
# 왜 while 씀?