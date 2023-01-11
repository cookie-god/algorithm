import sys
from collections import deque

def checkBorder(x, y):
    if x < 0 or x >= N or y < 0 or y >= N:
        return False
    return True


def bfs(x, y, index):
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    united = []  # 연합나라 좌표 저장하는 배열
    united.append((x, y))  # 좌표 저장
    check[x][y] = index  # 연합팀 종류 기록
    summary = array[x][y]  # 추후에 연합한 나라들의 인구수 합이 저장되는 변수
    count = 1  # 연합 나라
    queue = deque()
    queue.append((x, y))  # 큐 삽입

    while queue:
        a, b = queue.popleft()
        for i in range(4):
            na = a + dx[i]
            nb = b + dy[i]

            if checkBorder(na, nb):
                if check[na][nb] == -1:  # 연합이 되지 않은 나라인 경우
                    if L <= abs(array[na][nb] - array[a][b]) <= R:  # 두 나라 사이의 인구수가 L과 R사이에 있는 경우
                        queue.append((na, nb))  # 큐 삽입
                        check[na][nb] = index  # 연합 기록
                        summary += array[na][nb]  # 연합한 나라의 인구수 추가
                        count += 1  # 연합한 나라수 추가
                        united.append((na, nb))  # 연합 나라 좌표 저장

    # 인구수 재배치
    for i, j in united:
        array[i][j] = summary // count

N, L, R = map(int, sys.stdin.readline().split())
array = []
for i in range(N):
    array.append(list(map(int, sys.stdin.readline().split())))

totalCount = 0  # 전체 이동 횟수
while True:
    check = [[-1] * N for _ in range(N)]  # 연합 위치를 기록하는 배열
    index = 0  # 연합의 팀 종류를 나타내는 index
    # 전체 탐색
    for i in range(N):
        for j in range(N):
            if check[i][j] == -1:  # 연합이 되지 않은 곳이면 bfs 수행
                bfs(i, j, index)
                index += 1  # 연합팀 종류 증가
    if index == N * N:  # 모든 나라들이 연합을 해서 인구이동을 마쳤을 때
        break
    totalCount += 1  # 전체 이동횟수 증가

print(totalCount)

