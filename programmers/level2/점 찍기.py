import math
from collections import deque

# 경계선 체크
def checkBorder(x, y, max):
    if x < 0 or x > max or y < 0 or y > max:
        return False
    return True


# 거리 구하는 함수
def getDistance(x, y):
    return math.sqrt((x - 0) ** 2 + (y - 0) ** 2)


# bfs 탐색
def bfs(x, y, visited, k, d):
    dx = [-1, 1, 0, 0]  # x방면 이동
    dy = [0, 0, -1, 1]  # y방면 이동

    queue = deque()  # 큐 생성
    queue.append((x, y))  # 큐 삽입
    visited[x][y] = 1  # 방문 기록
    result = 1  # 정답 1로 초기화

    while queue:
        a, b = queue.popleft()
        for i in range(4):
            na = a + (dx[i] * k)  # k만큼 이동
            nb = b + (dy[i] * k)  # k만큼 이동

            if checkBorder(na, nb, d):
                if visited[na][nb] == 0 and getDistance(na, nb) <= d:  # 방문한 적 없고, 거리가 d미만인 경우
                    queue.append((na, nb))  # 큐삽입
                    visited[na][nb] = 1  # 방문 기록
                    result += 1  # 정답 추가

    return result


# 한개빼고 시간 초과
def solution1(k, d):
    answer = 0
    visited = [[0] * (d + 1) for _ in range(d + 1)]
    answer = bfs(0, 0, visited, k, d)

    return answer


# 4개빼고 시간 초과
def solution2(k, d):
    answer = 0

    for x in range(0, d + 1, k):  # k step만큼 비교
        maxY = math.floor(int(math.sqrt(d ** 2 - x ** 2)))  # 최대 max y값은 d(거리)^2 - x의 좌표^2의 루트하고 내림한 값
        for y in range(0, maxY + 1, k):  # k step만큼 허용 y값 추가
            answer += 1

    return answer


# 성공
def solution3(k, d):
    answer = 0

    for x in range(0, d + 1, k):
        maxY = math.floor(int(math.sqrt(d ** 2 - x ** 2)))   # 최대 max y값은 d(거리)^2 - x의 좌표^2의 루트하고 내림한 값
        answer += (maxY // k) + 1  # k 스템만큼 나누고 난 뒤 더하기 1(y좌표가 0인 경우 추가)

    return answer

print(solution1(2, 4))
print(solution1(1, 5))

print(solution2(2, 4))
print(solution2(1, 5))

print(solution3(2, 4))
print(solution3(1, 5))