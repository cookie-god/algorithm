# import sys
#
# def checkBorder(x, y):
#     if x < 0 or x >= N or y < 0 or y >= N:
#         return False
#     return True
#
#
# def solve(x, y, value):
#     for i in range(4):
#         nx = x + dx[i]
#         ny = y + dy[i]
#
#         if checkBorder(nx, ny):
#             if array[nx][ny] == 0 and visited[nx][ny] == 0:
#                 array[nx][ny] = value
#                 visited[nx][ny] = value
#
#
# N, K = map(int, sys.stdin.readline().split())
# array = []
#
# for i in range(N):
#     data = list(map(int, sys.stdin.readline().split()))
#     array.append(data)
# S, X, Y = map(int, sys.stdin.readline().split())
# dx = [0, 0, -1, 1]
# dy = [-1, 1, 0, 0]
#
# for i in range(S):
#     visited = [[0] * N for _ in range(N)]
#     for j in range(N):
#         for k in range(N):
#             if array[j][k] != 0 and visited[j][k] == 0:
#                 solve(j, k, array[j][k])
#
# print(array[X-1][Y-1])

import sys
from collections import deque

# 인덱스 체크 함수
def checkBorder(x, y):
    if x < 0 or x >= N or y < 0 or y >= N:
        return False
    return True


N, K = map(int, sys.stdin.readline().split())
array = []
for i in range(N):
    array.append(list(map(int, sys.stdin.readline().split())))

data = []
# 바이러스의 정보 담음
for i in range(N):
    for j in range(N):
        if array[i][j] != 0:
            data.append((array[i][j], 0, i, j))  # 바이러스 정보, 초, 행 위치, 열 위치

data.sort()  # 낮은 번호의 바이러스부터 전염을 시작하기 때문
queue = deque(data)  # 큐에 삽입

S, X, Y = map(int, sys.stdin.readline().split())
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

while queue:
    virus, s, x, y = queue.popleft()  # 큐에서 데이터 추출

    if s == S:  # 바이러스의 초와 종료 시간과 같으면 탈출
        break

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if checkBorder(nx, ny):  # 인덱스가 넘어버리지 않는다면
            if array[nx][ny] == 0:
                array[nx][ny] = virus  # 바이러스 전염
                queue.append((virus, s + 1, nx, ny))  # 큐에 새로운 데이터 삽입

print(array[X-1][Y-1])