import heapq


def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)

    while scoville:
        hot1 = heapq.heappop(scoville)

        if hot1 >= K:
            break

        if scoville:
            hot2 = heapq.heappop(scoville)
            answer += 1
            heapq.heappush(scoville, hot1 + (hot2 * 2))
        else:
            return -1
    return answer
