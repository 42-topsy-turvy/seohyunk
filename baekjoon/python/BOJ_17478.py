# BOJ 17478 재귀함수가 뭔가요?

N = int(input())
question = "어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다.\n"
prompt_1 = "\"재귀함수가 뭔가요?\"\n"
prompt_2 = "\"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.\n"
prompt_3 = "마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.\n"
prompt_4 = "그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어.\"\n"
prompt_5 = "라고 답변하였지."
answer = "\"재귀함수는 자기 자신을 호출하는 함수라네\""
print(question)

def recursive(N):
    i = 0
    if N == 0:
        print("____" * i + prompt_1)
        print("____" * i + answer)

    else:
        print("____" * i + prompt_1)
        print("____" * i + prompt_2)
        print("____" * i + prompt_3)
        print("____" * i + prompt_4)
        i = i + 1
        N = N - 1


import sys

N = int(sys.stdin.readline())
print("어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다.")
question = '"재귀함수가 뭔가요?"'
str1 = '"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.'
str2 = '마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.'
str3 = '그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어."'
string_end = "라고 답변하였지."


def recursive(k):
    global N
    print("____" * k + question)
    if k == N:
        print("____" * k + '"재귀함수는 자기 자신을 호출하는 함수라네"')
    else:
        print("____" * k + str1)
        print("____" * k + str2)
        print("____" * k + str3)
        recursive(k+1)

    print("____" * k + string_end)


recursive(0)
