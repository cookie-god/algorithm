import heapq
import sys

INF = int(1e9)

n, m = map(int, sys.stdin.readline().split())
start = int(sys.stdin.readline().strip())
graph = [[] for _ in range(n + 1)]
distance = [INF] * (n + 1)

for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a].append((b, c))

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))  # 시작 노드로 가기 위한 최단 경로는 0이고 큐에 삽입
    distance[start] = 0  # 시작 노드 최단 경로는 0

    while q:
        dist, now = heapq.heappop(q)  # 가장 최단 거리가 짧은 노드에 대한 정보 추출
        if distance[now] < dist:  # 현재 노드가 이미 처리된 적이 있는 노드라면 무시
            continue
        # 현재 노드와 연결된 다른 인접한 노드들 확인
        for item in graph[now]:
            cost = dist + item[1]  # 현재 노드 거쳐서 다른 노드로 이동하는 비용

            if cost < distance[item[0]]:  # 현재 노드를 거쳐서 다른 노드로 이동하는 비용이 더 작은 경우
                distance[item[0]] = cost  # 비용 최신화
                heapq.heappush(q, (cost, item[0]))  # 큐 삽입

dijkstra(start)

for i in range(1, n + 1):
    if distance[i] == INF:  # 접근할 수 없다면
        print('INFINITY')
    else:
        print(distance[i])  # 접근할 수 있다면

# 예제
# 6 11
# 1
# 1 2 2
# 1 3 5
# 1 4 1
# 2 3 3
# 2 4 2
# 3 2 3
# 3 6 5
# 4 3 3
# 4 5 1
# 5 3 1
# 5 6 2
# 3 3 4
# 3 3 5