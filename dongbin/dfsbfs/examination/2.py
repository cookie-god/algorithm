import sys
from collections import deque
from itertools import combinations
import copy

def checkBorder(x, y):
    if x < 0 or x >= N or y < 0 or y >= M:
        return False
    return True

def bfs(x, y, temp):
    queue = deque()
    queue.append([x, y])
    num = 0

    while queue:
        data = queue.popleft()
        a, b = data[0], data[1]
        for i in range(4):
            na = a + dx[i]
            nb = b + dy[i]

            if checkBorder(na, nb):
                if temp[na][nb] == 0:
                    queue.append([na, nb])
                    temp[na][nb] = 2

    print(temp)
    return num



def solve():
    result = 0
    for wall in candidate:
        temp = copy.deepcopy(array)
        safeAreaCount = 0
        for x, y in wall:
            temp[x][y] = 1

        for i in range(N):
            for j in range(M):
                if array[i][j] == 2:
                    safeAreaCount += bfs(i, j, temp)

        result = max(result, safeAreaCount)



N, M = map(int, sys.stdin.readline().split())
array = []
for i in range(N):
    array.append(list(map(int, sys.stdin.readline().split())))
empty = [(i, j) for i in range(N) for j in range(M) if array[i][j] == 0]
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

candidate = list(combinations(empty, 3))
solve()

