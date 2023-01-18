import sys
from collections import deque


def bfs(a, b):
    queue = deque()
    queue.append([a, b])
    visited[a][b] = 1
    visited[b][a] = 1

    while queue:
        data = queue.popleft()
        a, b = data[0], data[1]

        for index, value in enumerate(array[a]):
            if value == 1 and visited[b][index] == 0:
                visited[b][index] = 1
                visited[index][b] = 1
                queue.append([b, index])

    return True

N, M = map(int, sys.stdin.readline().split())
array = [[0] * N for _ in range(N)]
visited = [[0] * N for _ in range(N)]
for i in range(M):
    a, b = map(int, sys.stdin.readline().split())
    array[a - 1][b - 1] = 1
    array[b - 1][a - 1] = 1
result = 0
for i in range(N):
    for j in range(N):
        if array[i][j] == 1 and visited[i][j] == 0:
            bfs(i, j)
            result += 1

print(result)