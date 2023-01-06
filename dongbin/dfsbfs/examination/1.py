# 메모리 초과
# import sys
# from collections import deque
#
# N, M, K, X = map(int, sys.stdin.readline().split())
# array = [[0] * N for _ in range(N)]
# visited = [0 for _ in range(N)]
#
# for _ in range(M):
#     x, y = map(int, sys.stdin.readline().split())
#     array[x - 1][y - 1] = 1
#
# queue = deque()
# queue.append(X - 1)
# distance = 0
#
# while queue:
#     data = queue.popleft()
#     distance += 1
#     for i in range(N):
#         if i == data:
#             continue
#
#         if array[data][i] != 0:
#             if visited[i] != 0:
#                 visited[i] = min(visited[i], distance)
#             else:
#                 visited[i] = distance
#             queue.append(i)
#
# if K not in visited:
#     print(-1)
# else:
#     for i in range(N):
#         if visited[i] == K:
#             print(i + 1)

# import sys
#
# def dfs(start, distance):
#     distance += 1
#
#     for i in range(N):
#         if array[i][0] == start:
#             if visited[array[i][1]] != 0:
#                 visited[array[i][1]] = min(visited[array[i][1]], distance)
#             else:
#                 visited[array[i][1]] = distance
#             dfs(array[i][1], distance)
#
#
# N, M, K, X = map(int, sys.stdin.readline().split())
# visited = [0 for _ in range(N)]
#
# array = []
# for _ in range(M):
#     x, y = map(int, sys.stdin.readline().split())
#     array.append([x - 1, y - 1])
#
# distance = 0
# dfs(X-1, 0)
#
# result = []
# if X not in visited:
#     print(-1)
# else:
#     for i in range(N):
#         if visited[i] == K:
#             result.append(i + 1)
#     result.sort()
#     for num in result:
#         print(num)

from collections import deque
import sys

n, m, k, x = map(int, sys.stdin.readline().strip().split())
graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, sys.stdin.readline().strip().split())
    graph[a].append(b)  # 도로 정보 입력

distance = [-1]*(n+1)  # -1로 초기화
distance[x] = 0  # 출발 위치는 0으로 초기화

def bfs():
    queue = deque([x])  # x 값을 큐에 삽입

    while queue:
        now = queue.popleft()  # 큐에서 나온 데이터는 출발 도시

        for i in graph[now]:  # 출발 도시에서 연결되어있는 도시 찾기
            if distance[i] == -1:  # 방문하지 않은 도시인 경우
                distance[i] = distance[now]+1  # 거리 증가 시켜줌
                queue.append(i)  # 큐에 삽입

bfs()

if k not in distance:  # k만큼 떨어진 도시가 없는 경우
    print(-1)
else:  # k만큼 떨어진 도시가 있는 경우
    for i in range(1, n + 1):
        if distance[i] == k:
            print(i)