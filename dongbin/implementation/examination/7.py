import sys
from itertools import combinations

N, M = map(int, sys.stdin.readline().split())
array = []
for i in range(N):
    array.append(list(map(int, sys.stdin.readline().split())))
houses = []
chickenStores = []

# 집과 치킨집 좌표 튜플 형태로 저장
for i in range(N):
    for j in range(N):
        if array[i][j] == 1:
            houses.append((i, j))
        elif array[i][j] == 2:
            chickenStores.append((i, j))

# 순서가 상관 없으므로 combination으로 경우의 수 나열
totalCaseChickenStores = combinations(chickenStores, M)
result = 100000  # 비교를 위해 큰 수 대입

for chicken in totalCaseChickenStores:  # combination으로 나온 모든 경우의 수의 치킨집 좌표
    distance = 0  # 거리 초기화
    for house in houses:  # 모든 집들에 대해서 하나의 치킨집 경우의 수 길이 조사
        houseChickenInterval = 100000  # 집과 치킨집 간격 초기화
        for j in range(M):  # 치킨집 M개에 대해서 길이를 측정하기 위한 for문
            houseChickenInterval = min(houseChickenInterval, abs(house[0] - chicken[j][0]) + abs(house[1] - chicken[j][1]))  # 치킨집들 중에서 가장 집과 가까운 치킨집 거리 계산
        distance += houseChickenInterval  # 집과 가장 가까운 치킨집 거리 추가
    result = min(result, distance)  # 치킨집에 대해서 모두 집과 가장 가까운 거리들이 더해짐

print(result)