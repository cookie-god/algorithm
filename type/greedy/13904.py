import sys

N = int(sys.stdin.readline().strip())
homework = []
done = []  # 수행도가 가장 좋은 숙제들의 점수를 모아두는 변수
temp = []  # 수행 가능한 숙제들의 인덱스와 점수를 모아두는 변수
doneMaxIdx = 0
doneMaxScore = 0

for _ in range(N):
    d, w = map(int, sys.stdin.readline().split())
    homework.append((d, w))

homework.sort(key=lambda x: (-x[0], -x[1]))  # 일수 내림차순으로 정렬후, 같은 점수면 추가로 내림차순으로 정렬
day = homework[0][0]  # 마지막 날짜 저장

while True:
    #  탈출 조건
    if day == 0:
        break

    temp = []  # 초기화
    idx = 0  # 인덱스 위치 저장
    doneMaxIdx = 0  # 초기화
    doneMaxScore = 0  # 초기화
    for item in homework:
        if item[0] >= day:
            temp.append((idx, item[1]))  # temp 배열에 인덱스와 점수 추가
        idx += 1

    #  수행 가능한 날짜가 없다면
    if len(temp) == 0:
        idx = -1
    else:
        doneMaxIdx, doneMaxScore = max(temp, key=lambda x: x[1])  # 가장 높은 점수의 인덱스와 점수 저장
        homework.pop(doneMaxIdx)  # 리스트에서 제거
        done.append(doneMaxScore)  # 진행한 숙제에 점수 추가

    day -= 1  # 날짜 낮추기

print(sum(done))