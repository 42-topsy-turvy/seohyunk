# BOJ 4673 셀프 넘버

def self_number():
    num = 1
    print(1)
    while(True):
        for i in range(len(list(str(num)))):
            num += eval(list(str(num))[i])
        if num > 10000:
            break
        print(num)

self_number()