import sys
import copy
from itertools import combinations

# 경계값 체크
def checkBorder(x, y):
    if x < 0 or x >= N or y < 0 or y >= N:
        return False
    return True


# 학생을 마주칠 수 있는지 체크하는 함수
def solution(x, y, check):
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0 ,0]

    for i in range(4):
        nx, ny = x, y
        while True:
            nx += dx[i]
            ny += dy[i]

            if checkBorder(nx, ny):  # 경계선 체크해서 알맞다면
                if check[nx][ny] == 'S':  # 학생인 경우 False
                    return False
                elif check[nx][ny] == 'O':  # 장애물인 경우 break해서 새로운 방향 탐색
                    break
                elif check[nx][ny] == 'T':  # 선생님인 경우 break해서 새로운 방향 탐색
                    break
            else:  # 경계선 체크해서 알맞지 않는다면
                break
    return True


N = int(sys.stdin.readline().strip())
array = []
for i in range(N):
    array.append(list(map(str, sys.stdin.readline().split())))
none = []
# X의 좌표들 리스트에 저장
for i in range(N):
    for j in range(N):
        if array[i][j] == 'X':
            none.append((i, j))

# 콤비네이션을 통해 3개의 좌표 조합 리스트 생성
candidates = list(combinations(none, 3))

# 후보들에 대해서 반복문 수행
for candidate in candidates:
    temp = copy.deepcopy(array)  # 기존 배열을 깊은 복사를 통해서 저장
    for item in candidate:  # 장애물 설치
        temp[item[0]][item[1]] = 'O'
    answer = True  # flag 배열 조사할 때 쓰이는 값
    flag = []  # 모든 선생님들에 있어서 마주치지 않는지 체크
    for i in range(N):
        for j in range(N):
            if temp[i][j] == 'T':  # 선생님인 경우 함수 수행후 반환값 flag 배열에 저장
                flag.append(solution(i, j, temp))

    # flag 배열중 False가 있다면 정답 아님
    for i in range(len(flag)):
        if flag[i] != True:
            answer = False
            break
    # flag 배열 모두 True이면 탈출
    if answer:
        break

# 정답에 따라서 노출 변경
if answer:
    print('YES')
else:
    print('NO')