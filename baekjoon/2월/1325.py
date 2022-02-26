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
from collections import deque
import sys

input = sys.stdin.readline

def bfs(x):
    q = deque()
    c = [0 for _ in range(n)]
    q.append(x)
    c[x] = 1
    cnt = 1
    while q:
        x = q.popleft()
        for nx in a[x]:
            if c[nx] == 0:
                cnt += 1
                c[nx] = 1
                q.append(nx)
    return cnt

n, m = map(int, input().split())
a = [[] for _ in range(n)]

for _ in range(m):
    x, y = map(int, input().split())
    a[y-1].append(x-1)

ans = [0 for _ in range(n)]
for i in range(n):
    ans[i] = bfs(i)
for i in range(n):
    if ans[i] == max(ans):
        print(i+1, end=' ')