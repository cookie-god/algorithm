from collections import deque


def solution(maps):
    answer = 0
    row = len(maps)  # 행
    column = len(maps[0])  # 열
    visited = [[-1 for _ in range(column)] for _ in range(row)]  # 초기값 -1로 셋팅
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    def checkBorder(x, y):  # 경계선 체크
        if 0 <= x < row and 0 <= y < column:
            return True
        return False

    def bfs(x, y):
        queue = deque()
        queue.append((x, y))
        visited[x][y] = 1  # 방문 기록 체크
        while queue:
            a, b = queue.popleft()
            for i in range(4):
                na = a + dx[i]
                nb = b + dy[i]
                if checkBorder(na, nb):
                    if maps[na][nb] == 1 and visited[na][nb] == -1:
                        queue.append((na, nb))
                        visited[na][nb] = visited[a][b] + 1  # 방문 기록 추가

    bfs(0, 0)  # 첫번째 위치에서 시작
    answer = visited[row - 1][column - 1]  # 도착지에 셋팅된 방문기록 정답
    return answer