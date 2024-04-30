# BOJ 13305 주유소

import sys
N = int(sys.stdin.readline())
length_list = list(map(int, sys.stdin.readline().split()))
price_list = list(map(int, sys.stdin.readline().split()))

# [2, 3, 1]
# [5, 2, 4, 1]

gas_price = price_list[0] * length_list[0]
min_unit_price = price_list[0]

for i in range(1, len(price_list) - 1):
    if(price_list[i] <= price_list[i - 1]):
        min_unit_price = min(price_list[i], min_unit_price)
#        print("min", min_unit_price)
        gas_price += min_unit_price * length_list[i]
#        print(i, "sum ", gas_price)
    else: # price_list[i] > price_list[i - 1]
        min_unit_price = min(min_unit_price, price_list[i - 1])
#        print("min", min_unit_price)
        gas_price += min_unit_price * length_list[i]
#        print(i, "sum ", gas_price)

print(i, gas_price)
