import heapq


def solution(n, k, enemy):
    answer = 0
    heap = []
    for i, e in enumerate(enemy):
        heapq.heappush(heap, e)
        if len(heap) > k:  # 원소의 개수가 k보다 큰 경우, 가장 큰값 뺄 수 있음
            n -= heapq.heappop(heap)  # 항상 큰 수 제외하고 사용함
        if n < 0:
            return i

    return len(enemy)