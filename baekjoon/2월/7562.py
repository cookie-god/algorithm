import sys
from collections import deque

def checkIndex(x, y, N): #인덱스 체크하는 함수
    if x >= N or x < 0 or y >= N or y < 0:
        return False
    return True

K = int(sys.stdin.readline())
dx = [-2, -1, -2, -1, 2, 1, 2, 1] #x방향 리스트
dy = [-1, -2, 1, 2, -1, -2, 1, 2] #y방향 리스트

result = []
for i in range(K):
    N = int(sys.stdin.readline())
    visited = [[0]*N for _ in range(N)] #방문 기록 체크
    flag = 0 #도착지점에 이미 도착했는지 체크하는 변수
    a, b = map(int, sys.stdin.readline().split()) #첫 위치
    reachX, reachY = map(int, sys.stdin.readline().split()) #도착 지점
    if a == reachX and b == reachY: #처음부터 같다면 답은 0
        result.append(0)
    else:
        queue = deque()  # queue 선언
        queue.append((a, b)) # push
        while queue:
            x, y = queue.popleft()
            for i in range(8): #8방향 체크
                tmpX = x + dx[i]
                tmpY = y + dy[i]
                if checkIndex(tmpX, tmpY, N): #인덱스 체크하는 함수
                    if visited[tmpX][tmpY] == 0 : #방문한 적 없는 경우
                        visited[tmpX][tmpY] = visited[x][y] + 1
                        if tmpX == reachX and tmpY == reachY: #만약에 도착지점에 도달했다면
                            result.append(visited[reachX][reachY]) #정답 리스트에 추가
                            flag = 1 #도착완료 변수 추가
                            break
                        queue.append((tmpX, tmpY)) # push
            if flag == 1: #이미 도착했으면 break
                break
        if flag == 0:
            result.append(visited[reachX][reachY]) #정답에 삽입

for i in range(K):
    print(result[i])