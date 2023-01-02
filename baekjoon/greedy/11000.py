import sys
import heapq
# 우선순위큐를 사용하는 이유
# 1. 큐를 이용해서, 종료시간을 저장해야함
# 2. 큐 삽입시, 가장 먼저 종료되는 강의를 순서대로 배치를 해야하기 때문에 큐중에서 우선순위큐를 사용함

N = int(sys.stdin.readline().strip())
arr = []

for i in range(N):
    a, b = map(int, sys.stdin.readline().split())
    arr.append((a, b))

# 강의 시작시간에 따라 정렬
arr.sort(key=lambda x: x[0])

# 강의 종료시간 힙큐로 저장
lecture = []
heapq.heappush(lecture, arr[0][1])

for i in range(1, N):
    if arr[i][0] < lecture[0]:  # 새로운 강의의 시작시간이 기존 강의의 종료시간보다 작으면
        heapq.heappush(lecture, arr[i][1])  # 새로운 강의의 종료시간 push
    else:  # 새로운 강의의 시작시간이 기존 강의의 종료시간보다 크거나 같다면
        heapq.heappop(lecture)  # 힙큐에서 pop
        heapq.heappush(lecture, arr[i][1])  # 새로운 강의의 종료시간 push

print(len(lecture))