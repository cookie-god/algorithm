import sys


def checkBorder(x, y):
    if x < 0 or x >= N or y < 0 or y >= M:
        return False
    return True


N, M = map(int, sys.stdin.readline().split())
a, b, d = map(int, sys.stdin.readline().split())
array = []
for i in range(N):
    array.append(list(map(int, sys.stdin.readline().split())))
visited = [[0] * N for _ in range(N)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

visited[a][b] = 1
count = 1
check = 0

while True:
    # 왼쪽으로 도는 로직
    d -= 1
    if d == -1:  # -1이면 3으로 변경
        d = 3

    na = a + dx[d]
    nb = b + dy[d]
    # 경계값 체크
    if not checkBorder(na, nb):
        check += 1
    else:
        if array[na][nb] == 0 and visited[na][nb] == 0:  # 육지이고 방문한 이력이 없는 경우
            a = na
            b = nb
            visited[a][b] = 1  # 방문기록 남기기
            check = 0  # 네방향 체크 초기화
            count += 1
        else:
            check += 1

    if check == 4:  # 네방향 모두 체크한 경우
        na = a - dx[d]
        nb = b - dx[d]  # 현재 방향에서 뒤로 한걸음 돌아가기
        if array[na][nb] == 0:  # 뒤로 돌아가는 방향이 육지인 경우 돌아가기 가능
            a = na
            b = nb
        else:  # 바다라면 돌아가기 불가능
            break
        check = 0  # 네방향 체크 초기화

print(visited)
print(count)