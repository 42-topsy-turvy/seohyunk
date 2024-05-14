# def solution(scoville, K):
#     answer = 0
#     scoville = sorted(scoville)
#     while min(scoville) < K:
#         if len(scoville) == 1:
#             return -1
#         scoville[0] = scoville[0] + scoville[1] * 2
#         del(scoville[1])
#         answer += 1
#         scoville = sorted(scoville)
#     return answer
# 시간초과

import heapq


def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    while scoville[0] < K:
        if len(scoville) == 1:
            return -1
        heapq.heappush(scoville, heapq.heappop(scoville) + heapq.heappop(scoville) * 2)
        answer += 1

    return answer