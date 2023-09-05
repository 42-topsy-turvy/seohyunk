'''폴리오미노'''
Board = input()

Board = Board.replace('XXXX', 'AAAA')
Board = Board.replace('XX', 'BB')

if 'X' in Board:
    print(-1)
else:
    print(Board)

# count = 0
# ans_list = []
#
# if '.' in Board:
#     Splited_Board = Board.split('.')
#     for i in Splited_Board:
#         X_num = i.count('X')
#         if X_num % 2 != 0:
#             print(-1)
#             break
#         if X_num % 4 == 0:
#             i = i.replace('X', 'A')
#             ans_list.append(i)
#         elif X_num == 2:
#             i = i.replace('X', 'B')
#             ans_list.append(i)
# else:
#     Splited_Board = list(map(''.join, zip(*[iter(Board)]*2)))
#
# print('.'.join(ans_list))
