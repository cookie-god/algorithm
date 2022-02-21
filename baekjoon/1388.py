import sys

def dfs(x, y):
    visited[x][y] = 1 #방문 기록
    if flag == 0: #'-'인 경우
        if y + 1 != M: #인덱스 넘는지 체크
            if array[x][y+1] == '-': #다음번 애가 -인 경우엔 함수 호출
                dfs(x,y+1)
        return #다시 돌아가기
    else: #'|'인 경우
        if x + 1 != N: #인덱스 넘는지 체크
            if array[x+1][y] == '|': #다은번 애가 |인 경우엔 함수 호출
                dfs(x+1, y)
        return #다시 돌아가기

N, M = map(int, sys.stdin.readline().split()) #N, M 입력 받음
array = [] #배열
visited = [[0]*M for _ in range(N)] #방문기록 체크
for i in range(N): #입력
    array.append(sys.stdin.readline().strip())

result = 0 #결과값
flag = 0 # - or | flag 값

for i in range(N):
    for j in range(M):
        if visited[i][j] == 0: #방문한적이 없는 경우
            if array[i][j] == '-': #-이면 flag = 0
                flag = 0
            else: #'|'이면 flag = 1
                flag = 1
            dfs(i, j) #dfs함수 호출
            result += 1 #최종적으로 돌아온 경우 +1
print(result)