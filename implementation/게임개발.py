N, M = map(int, input().split())
x, y, direction = map(int, input().split())
arr = []
for i in range(N):
    arr.append(list(map(int, input().split())))

visited = [[0] * M for _ in range(N)]
visited[x][y] = 1 #방문 기록 남김
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
#북, 동, 남, 서

count = 1 #이동횟수
turn = 0 #회전횟수

#인덱스 오류를 해결하기 위한 함수
def checkValid(x, y):
    if x < 0 or x >= M or y < 0 or y >= N:
        return False
    return True

#무한루프 반복문을 만든 뒤, 탈출 조건을 세워줌
while True:
    direction -= 1 #시계 반대방향으로 회전
    turn += 1 #회전 횟수 증가
    if direction < 0: #서쪽을 보기 위한 분기처리
        direction = 3

    tmpX = x + dx[direction]
    tmpY = y + dy[direction]

    if checkValid(tmpX, tmpY): #인덱스 오류 체크
        if arr[tmpX][tmpY] == 0 and visited[tmpX][tmpY] == 0: #육지이고 방문한 적이 없는 경우
            x = tmpX
            y = tmpY
            visited[x][y] = 1 #방문 기록 저장
            count += 1 #이동가능 횟수 카운트
            turn = 0 #회전횟수 초기화

        if turn == 4: #4방향 다 본 경우
            tmpX = x - dx[direction]
            tmpY = y - dy[direction] #보고있는 방향에서 뒤로 이동
            if checkValid(tmpX, tmpY): #인덱스 오류 체크
                if arr[tmpX][tmpY] == 0: #이전으로 돌아갈 수 있다면
                    x = tmpX
                    y = tmpY
                    turn = 0
                else:
                    break
            else:
                break

print(count)







