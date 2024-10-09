from collections import deque


def checkBorder(maxX, maxY, x, y):
    if 0 <= x < maxX and 0 <= y < maxY:
        return True
    return False


def bfs(array, visited, x, y, flag):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    queue = deque()
    queue.append((x, y))
    while queue:
        a, b = queue.popleft()
        for i in range(4):
            na, nb = a + dx[i], b + dy[i]
            if checkBorder(len(array), len(array[0]), na, nb):
                if array[na][nb] == "O":
                    if visited[na][nb] == 0:
                        visited[na][nb] = visited[a][b] + 1
                        queue.append((na, nb))
                elif array[na][nb] == "S":
                    if visited[na][nb] == 0:
                        visited[na][nb] = visited[a][b] + 1
                        queue.append((na, nb))
                elif array[na][nb] == "L":
                    if visited[na][nb] == 0:
                        temp = visited[a][b] + 1
                        for i in range(len(visited)):
                            for j in range(len(visited[0])):
                                visited[i][j] = 0
                        visited[na][nb] = temp
                        flag = True
                        queue.clear()
                        queue.append((na, nb))
                        break
                elif array[na][nb] == "E":
                    visited[na][nb] = visited[a][b] + 1
                    if (flag == True):
                        return visited[na][nb]
                    queue.append((na, nb))
    return -1


def solution(maps):
    answer = 0
    flag = False
    visited = [[0] * len(maps[0]) for _ in range(len(maps))]

    for i in range(len(maps)):
        for j in range(len(maps[i])):
            if (maps[i][j] == "S"):
                answer = bfs(maps, visited, i, j, flag)

    print(visited)
    return answer