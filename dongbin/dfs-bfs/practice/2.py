import sys
from collections import deque
import time

def checkBorder(x, y):
    if x < 0 or x >= N or y < 0 or y >= M:
        return False
    return True

def bfs():
    queue = deque()
    queue.append([0, 0])
    bfsVisited[0][0] = 1
    while queue:
        data = queue.popleft()
        a, b = data[0], data[1]

        for i in range(4):
            na, nb = a + dx[i], b + dy[i]
            if checkBorder(na, nb):
                if bfsArray[na][nb] == 1 and bfsVisited[na][nb] == 0:
                    bfsVisited[na][nb] = bfsVisited[a][b] + 1
                    queue.append([na, nb])

def dfs(x, y, n):
    if not checkBorder(x, y):
        return False

    if dfsArray[x][y] != 1:
        return False

    if dfsVisited[x][y] != 0:
        dfsVisited[x][y] = min(dfsVisited[x][y], n + 1)
        return False
    else:
        dfsVisited[x][y] = n + 1

    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        dfs(nx, ny, dfsVisited[x][y])
    return True


N, M = map(int, sys.stdin.readline().split())
bfsArray = []
for i in range(N):
    bfsArray.append(list(map(int, sys.stdin.readline().strip())))
dfsArray = bfsArray.copy()
bfsVisited = [[0] * M for _ in range(N)]
dfsVisited = [[0] * M for _ in range(N)]
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

curTime = time.time()
bfs()
print(time.time() - curTime)
print(bfsVisited[N-1][M-1])

curTime = time.time()
dfs(0, 0, 0)
print(time.time() - curTime)
print(dfsVisited[N-1][M-1])

