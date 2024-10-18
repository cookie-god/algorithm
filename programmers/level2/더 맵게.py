import heapq


def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)

    while scoville[0] < K:  # 가장 작은 값이 K보다 크다면 탈출
        if len(scoville) > 1:  # 길이가 1 이상인 경우에만
            heapq.heappush(scoville, heapq.heappop(scoville) + heapq.heappop(scoville) * 2)
            answer += 1
        else:  # K이상 만드는 것 실패
            answer = -1
            break

    return answer