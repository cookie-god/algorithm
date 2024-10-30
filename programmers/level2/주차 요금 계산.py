from collections import defaultdict
import math


def makeTimeMinute(time):  # 시간을 분으로 만드는 함수
    hour, minute = time.split(":")
    hour = int(hour)
    minute = int(minute)
    return hour * 60 + minute


def solution(fees, records):
    answer = []
    # fees 0: 기본 시간, 1: 기본 요금, 2: 단위 시간, 3: 단위 요금
    inDict = defaultdict(int)  # 들어온 경우 관리하는 딕셔너리
    resultDict = defaultdict(int)  # 차 별로 총 주차한 시간 관리하는 딕셔너리
    answerDict = defaultdict(int)  # 차 별로 총 주차비를 관리하는 딕셔너리

    for record in records:
        time, number, info = record.split(" ")
        time = makeTimeMinute(time)  # 시간으로 변경
        if info == "IN":  # IN이면 inDict에 삽입
            inDict[number] = time
        else:  # OUT이면 inDict의 value값이랑 현재 시간 빼서 resultDict에 삽입
            resultDict[number] += time - inDict[number]  # 주차 시관 관리하는 딕셔너리에 삽입
            del inDict[number]  # in 딕셔너리에서 제거

    if inDict:  # in 딕셔너리가 아직 있는 경우
        for key, value in inDict.items():
            resultDict[key] += 1439 - value  # 23:59에서 현재 시간 계산

    for key, value in resultDict.items():
        if value > fees[0]:  # 기본시간보다 크거나 같음
            answerDict[key] = fees[1] + math.ceil((value - fees[0]) / fees[2]) * fees[3]
        else:  # 기본시간보다 작거나 같음
            answerDict[key] = fees[1]  # 기본 요금

    answerDict = sorted(answerDict.items(), key=lambda x: x[0])
    for value in answerDict:
        answer.append(value[1])

    return answer