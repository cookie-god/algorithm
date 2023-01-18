import sys
from collections import deque
import time

def checkBorder(x, y):
    if x < 0 or x >= N or y < 0 or y >= M:
        return False
    return True


def bfs(a, b):
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    queue = deque()
    queue.append([a, b])
    bfsVisited[a][b] = 1

    while queue:
        data = queue.popleft()
        x = data[0]
        y = data[1]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if checkBorder(nx, ny):
                if bfsArray[nx][ny] == 0 and bfsVisited[nx][ny] == 0:
                    bfsVisited[nx][ny] = 1
                    queue.append([nx, ny])

def dfs(a, b):
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    if not checkBorder(a, b):
        return False

    if dfsArray[a][b] == 0 and dfsVisited[a][b] == 0:
        dfsVisited[a][b] = 1
    else:
        return False

    for i in range(4):
        na, nb = a + dx[i], b + dy[i]
        dfs(na, nb)

    return True


N, M = map(int, sys.stdin.readline().split())
bfsArray = []
for i in range(N):
    bfsArray.append(list(map(int, sys.stdin.readline().strip())))
dfsArray = bfsArray.copy()
bfsVisited = [[0] * M for _ in range(N)]
dfsVisited = [[0] * M for _ in range(N)]
bfsCount = 0
dfsCount = 0

curTime = time.time()
for i in range(N):
    for j in range(M):
        if bfsArray[i][j] == 0 and bfsVisited[i][j] == 0:
            bfs(i, j)
            bfsCount += 1
print(time.time() - curTime)
print(bfsCount)

curTime = time.time()
for i in range(N):
    for j in range(M):
        if dfsArray[i][j] == 0 and dfsVisited[i][j] == 0:
            if dfs(i, j) == True:
                dfsCount += 1

print(time.time() - curTime)
print(dfsCount)
