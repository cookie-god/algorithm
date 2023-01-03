import sys

N = int(sys.stdin.readline().strip())
K = int(sys.stdin.readline().strip())
array = [[0] * (N + 1) for _ in range(N + 1)]
for i in range(K):
    x, y = map(int, sys.stdin.readline().split())
    array[x][y] = 1
L = int(sys.stdin.readline().strip())
rotate = []
for i in range(L):
    x, y = map(str, sys.stdin.readline().split())
    rotate.append((int(x), y))

dx = [0, -1, 0, 1]
dy = [1, 0, -1, 0]
direction = 0 # 0은 동, 1은 북, 2는 서, 3은 남

x, y = 1, 1  # 초기 위치 저장
snakeBody = [(x, y)]  # 뱀 몸이 있는 위치 저장
time = 0  # 시간 저장

while True:
    # 현재 보고 있는 뱡향을 토대로 이동
    nx = x + dx[direction]
    ny = y + dy[direction]

    # 벽과 부딪힌 경우
    if nx < 1 or nx > N or ny < 1 or ny > N:
        time += 1
        break

    # 뱀의 몸과 부딪힌 경우
    if (nx, ny) in snakeBody:
        time += 1
        break

    if array[nx][ny] != 1:  # 사과가 아니라면 뱀 몸의 맨 처음 위치 제거
        snakeBody.pop(0)
    else:  # 사과라면 사과를 없애줌
        array[nx][ny] = 0

    snakeBody.append((nx, ny))  # 뱀의 몸 추가
    time += 1  # 시간 증가
    x, y = nx, ny  # x, y 최신화

    # 시간이 회전할 시간인지 체크
    for item in rotate:
        if time == item[0]:  # 만약에 회전할 시간이라면
            # L인 경우 반시계 방향
            if item[1] == 'L':
                if direction + 1 > 3:
                    direction = 0
                else:
                    direction += 1

            # D인 경우 시계 방향
            elif item[1] == 'D':
                if direction - 1 < 0:
                    direction = 3
                else:
                    direction -= 1
            break

print(time)