N = int(input())

'''
for i in range(len(a))를 실행하면 
i에는 요소가 아닌 0부터 마지막 index까지 
index가 들어감.
'''
cnt = 0
seat = input()
couple = seat.count("LL")
if couple == 0:
    print(N)
else:
    print(N - couple + 1)