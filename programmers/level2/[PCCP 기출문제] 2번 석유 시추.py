from collections import deque


def solution(land):
    answer = 0
    row = len(land)
    column = len(land[0])
    visited = [[0] * column for _ in range(row)]  # 방문 방향 체크를 위한 리스트
    locationList = [0 for _ in range(column)]  # 각 컬럼의 인덱스별 석유량 저장을 위한 리스트

    def bfs(x, y):
        dx = [0, 0, -1, 1]  # 4방향의 x축
        dy = [-1, 1, 0, 0]  # 4방향의 y축
        checkColumn = []  # 컬럼 위치 체크를 위한 리스트
        result = 0  # 석유량

        queue = deque()
        queue.append((x, y))  # 해당 위치 큐 삽입
        visited[x][y] = 1  # 방문 기록 표시
        checkColumn.append(y)  # 컬럼 위치 삽입
        result = result + 1  # 석유량 증가

        while queue:
            a, b = queue.popleft()
            for i in range(4):
                na, nb = a + dx[i], b + dy[i]  # 4방향 위치 이동
                if checkBorder(na, nb, row, column):  # 이동 가능 범주 체크
                    if land[na][nb] == 1 and visited[na][nb] == 0:  # 석유가 있는 곳이고 방문한 적이 없는 경우
                        visited[na][nb] = 1  # 방문기록 표시
                        result = result + 1  # 석유량 증가
                        checkColumn.append(nb)  # 컬럼 위치 삽입
                        queue.append((na, nb))  # 방문 큐 삽입

        checkColumn = list(set(checkColumn))  # 중복 제거
        for i in range(len(checkColumn)):
            locationList[checkColumn[i]] = locationList[checkColumn[i]] + result  # 컬럼 위치에 존재하는 위치에 석유량 추가

    def checkBorder(x, y, maxX, maxY):  # 이동 가능 범주 체크 함수
        if 0 <= x < maxX and 0 <= y < maxY:
            return True
        return False

    for i in range(row):
        for j in range(column):
            if land[i][j] == 1 and visited[i][j] == 0:  # 석유가 있고 방문한 적이 없는 경우
                bfs(i, j)  # 각 위치별 석유 매장위치 저장

    answer = max(locationList)  # 리스트중 가장 큰 값이 정답
    return answer

