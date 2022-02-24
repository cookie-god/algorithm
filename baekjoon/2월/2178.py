from collections import deque
import sys

def checkIndex(x, y): #인덱스 체크하는 함수
    if x >= N or x < 0 or y >= M or y < 0:
        return False
    return True

N, M = map(int, sys.stdin.readline().split())
dx = [-1, 1, 0, 0] #x방향 리스트
dy = [0, 0, -1, 1] #y방향 리스트
array = []
for i in range(N):
    array.append(list(map(int, sys.stdin.readline().strip())))
visited = [[0]*M for _ in range(N)] #방문기록 체크
queue = deque() #queue 선언
queue.append((0, 0)) #1행 1열 추가
visited[0][0] = 1 #방문기록 1증가

while queue: #큐가 채워져있을때 까지
    x, y = queue.popleft() #초기 x, y값 세팅
    for i in range(4): #4방향 접근(북, 남, 서, 동)
        tmpX = x + dx[i]
        tmpY = y + dy[i]
        if checkIndex(tmpX, tmpY):
            if array[tmpX][tmpY] != 0 and visited[tmpX][tmpY] == 0: #지날갈 수 있고, 이전에 방문한 적이 없는 경우
                queue.append((tmpX, tmpY)) #큐 추가
                visited[tmpX][tmpY] = visited[x][y] + 1 #이전 방문기록보다 1증가된 값으로 새로운 방문기록 등록

print(visited[N-1][M-1]) #마지막 행, 열값 출력