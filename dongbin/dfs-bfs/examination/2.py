import sys
import copy
from collections import deque
from itertools import combinations

# 경계선 체크
def checkBorder(x, y):
    if x < 0 or x >= N or y < 0 or y >= M:
        return False
    return True

# bfs 탐색
def bfs(x, y, temp):
    queue = deque()
    queue.append([x, y])  # 바이러스 x, y좌표 삽입

    # 큐가 빌때까지
    while queue:
        data = queue.popleft()
        a, b = data[0], data[1]  # x, y좌표 추출
        for i in range(4):  # 4방향 거리 이동
            na = a + dx[i]
            nb = b + dy[i]

            if checkBorder(na, nb):  # 경계선 체크
                if temp[na][nb] == 0:  # 바이러스와 벽이 아니라면
                    queue.append([na, nb])  # 큐 삽입
                    temp[na][nb] = 2  # 바이러스 감염

# 안전지역 개수 체크
def checkSafeArea(temp):
    num = 0
    for i in range(N):
        for j in range(M):
            if temp[i][j] == 0:
                num += 1
    return num

# solve 함수
def solve():
    result = 0  # 안전 지역 개수
    for wall in candidate:  # 벽 후보군들
        temp = copy.deepcopy(array)  # 배열에 벽을 새로 세우기 위해 깊은 복사
        for x, y in wall:  # 새로운 벽들에 대한 x, y 좌표
            temp[x][y] = 1  # 세로운 벽 세우기
        for i in range(N):
            for j in range(M):
                if array[i][j] == 2:  # 바이러스라면 bfs 진행
                    bfs(i, j, temp)
        safeAreaCount = checkSafeArea(temp)  # 전체 안전지역 개수 카운트
        result = max(result, safeAreaCount)  # 가장 많은 것 result에 대립
    return result



N, M = map(int, sys.stdin.readline().split())
array = []
for i in range(N):
    array.append(list(map(int, sys.stdin.readline().split())))
empty = [(i, j) for i in range(N) for j in range(M) if array[i][j] == 0]  # 안전지역에 대한 좌표들 튜플 리스트로 저장
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

candidate = list(combinations(empty, 3))  # 3개의 벽 후보 모든 좌표들 저장
print(solve())

