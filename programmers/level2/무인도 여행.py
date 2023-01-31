from collections import deque

# 경계값 체크
def checkBorder(x, y, maxX, maxY):
    if x < 0 or x >= maxX or y < 0 or y >= maxY:
        return False
    return True


# bfs 순회
def bfs(maps, visited, x, y, maxX, maxY):
    dx = [-1, 1, 0, 0]  # 네방향 문제 배열
    dy = [0, 0, -1, 1]  # 네방향 문제 배열
    count = int(maps[x][y])  # 머물수 있는 수 더해줌
    visited[x][y] = 1  # 방문 기록
    queue = deque()  # 큐 생성
    queue.append((x, y))  # 현재 좌표 삽입

    while queue:
        a, b = queue.popleft()  # 큐에서 데이터 추출
        for i in range(4):  # 네방향 체크
            na = a + dx[i]
            nb = b + dy[i]

            if checkBorder(na, nb, maxX, maxY):  # 경계선 벗어나는지 체크
                if maps[na][nb] != 'X' and visited[na][nb] == 0:  # X가 아니고 방문한 적 없는 경우
                    count += int(maps[na][nb])  # 머물수 있는 수 더해주기
                    queue.append((na, nb))  # 큐 삽입
                    visited[na][nb] = 1  # 방문기록 남기기

    return count


def solution(maps):
    answer = []
    mapsRow = len(maps)  # 행 길이
    mapsColumn = len(maps[0])  # 열 길이
    visited = [[0] * mapsColumn for _ in range(mapsRow)]  # 방문 기록 초기화

    for i in range(mapsRow):
        for j in range(mapsColumn):
            if maps[i][j] != 'X' and visited[i][j] == 0:  # X가 아니고 방문한 경험이 없는 경우
                answer.append(bfs(maps, visited, i, j, mapsRow, mapsColumn))

    answer.sort()  # 오름차순 정렬

    if len(answer) == 0:  # 무인도가 없는 경우
        answer.append(-1)
    return answer

print(solution(["X591X","X1X5X","X231X", "1XXX1"]))
print(solution(["XXX","XXX","XXX"]))