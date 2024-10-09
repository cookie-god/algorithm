from collections import deque


def solution(board):
    answer = -1
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    row = len(board)
    column = len(board[0])
    visited = [[0] * len(board[0]) for _ in range(len(board))]

    def bfs(x, y):
        visited[x][y] = 1  # 방문 기록 남김
        queue = deque()
        queue.append((x, y))

        while queue:
            nx, ny = queue.popleft()
            if board[nx][ny] == "G":
                return visited[nx][ny] - 1
            for i in range(4):
                a, b = nx, ny
                while True:
                    a, b = a + dx[i], b + dy[i]
                    if 0 <= a < row and 0 <= b < column and board[a][b] == "D":  # D인 경우, 이전으로 한칸 이덩
                        a -= dx[i]
                        b -= dy[i]
                        break
                    if a < 0 or a >= row or b < 0 or b >= column:  # 외벽인 경우, 이전으로 한칸 이덩
                        a -= dx[i]
                        b -= dy[i]
                        break
                if not visited[a][b]:  # 벽에 부딪혔을때 방문한 적이 없는 경우
                    visited[a][b] = visited[nx][ny] + 1
                    queue.append((a, b))
        return -1  # 못찾은 경우 -1 리턴

    for i in range(len(board)):
        for j in range(len(board[0])):
            if (board[i][j] == "R"):
                result = bfs(i, j)

    return result