def solution(phone_book):
    phone_book.sort()
    for i in range(len(phone_book) - 1):
        for j in range(len(phone_book) - 2):
            if phone_book[i] == phone_book[j + 1][:len(phone_book[i])]:
                answer = False

    answer = True
    return answer