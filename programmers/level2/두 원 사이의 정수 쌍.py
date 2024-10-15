import math

def solution(r1, r2):
    answer = 0
    r1List = [(x, y) for x in range(0, r1 + 1) for y in range(0, r1 + 1)] # r1 반지름 길이만큼 좌표 셋팅
    r1List = list(filter(lambda x: math.sqrt(x[0] ** 2 + x[1] ** 2) <= r1, r1List)) # r1 반지름 길이 내에 존재하는 데이터만 셋팅
    r2List = [(x, y) for x in range(0, r2 + 1) for y in range(0, r2 + 1)] # r2 반지름 길이만큼 좌표 셋팅
    r2List = list(filter(lambda x: math.sqrt(x[0] ** 2 + x[1] ** 2) <= r2, r2List)) # r2 반지름 길이 내에 존재하는 데이터만 셋팅
    answer = len(r2List) - len(r1List)
    return answer * 4
