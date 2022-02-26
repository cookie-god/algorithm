# import sys
# from collections import deque
#
# N, M = map(int, sys.stdin.readline().split())
# array = [[0]*(N+1) for _ in range(N+1)]
# result = [0 for _ in range(N)]
# # print(result)
# for i in range(M):
#     x, y = map(int, sys.stdin.readline().split())
#     # array[x][y] = 1
#     array[y][x] = 1
#
# for i in range(1, N+1):
#     visited = [[0] * (N + 1) for _ in range(N + 1)]
#     # print("-------")
#     for j in range(1, N+1):
#         queue = deque()  # queue 선언
#         if array[i][j] != 0 and  visited[i][j] == 0:
#             queue.append(j)
#             visited[i][j] = 1
#             visited[j][i] = 1
#             result[i-1] += 1
#             # print(i, j)
#             while queue:
#                 z = queue.popleft()
#                 for k in range(1, N+1):
#                     if array[z][k] != 0 and visited[z][k] == 0:
#                         queue.append(k)
#                         visited[z][k] = 1
#                         visited[k][z] = 1
#                         result[i-1] += 1
#                         # print(z, k)
#
# check = {}
# for i in range(N):
#     check[i+1] = result[i]
#
#
# sortedCheck = sorted(check.items())
# _, maxNum = sortedCheck[0]
# # print(maxNum)
#
# for (key, value) in sortedCheck:
#     if value == maxNum:
#         print(key, end=' ')
#
#

import sys

input = sys.stdin.readline  # 중요!!!!, 입력 속도가 느리면 통과 불가능.
from collections import deque


# 너비 우선 탐색
def bfs(s):
    D = 0
    q = deque()
    q.append(s)
    visit = [0] * (N + 1)
    visit[s] = 1
    while q:
        here = q.popleft()
        D += 1
        for w in G[here]:
            if not visit[w]:
                visit[w] = 1
                q.append(w)
    return D  # 방문한 정점의 수 D를 리턴한다.


N, M = map(int, input().split())
G = [[] for _ in range(N + 1)]
for i in range(M):
    a, b = map(int, input().split())
    G[b].append(a)
mxd = 0
result = []
for i in range(1, N + 1):
    if G[i]:
        tmp = bfs(i)  # 리턴값을 받아서 최대값과 비교
        if mxd <= tmp:
            if mxd < tmp:
                result = []
            mxd = tmp
            result.append(i)
print(*result)