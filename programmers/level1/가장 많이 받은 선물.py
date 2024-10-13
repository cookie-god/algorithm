from itertools import combinations


def solution(friends, gifts):
    answer = 0
    giftDict = {}  # 선물 전달 이력
    presentPower = {}  # 선물 지수
    nextPresent = {}  # 다음달 선물 받을 정보

    for friend in friends:  # 친구값에 따라 데이터 초기화
        giftDict[friend] = {f: 0 for f in friends}  # 딕셔너리 value도 또 딕셔너리
        presentPower[friend] = 0  # 초기값
        nextPresent[friend] = 0  # 초기값

    for gift in gifts:
        giver, taker = gift.split(" ")
        giftDict[giver][taker] += 1  # 선물준 이력 저장
        presentPower[giver] += 1  # 선물준 사람의 선물지수 증가
        presentPower[taker] -= 1  # 선물받은 사람의 선물지수 감소

    combinationFriends = list(combinations(friends, 2))  # 콤비네이션으로 2명의 관계 추출
    for friend in combinationFriends:
        if giftDict[friend[0]][friend[1]] > 0 or giftDict[friend[1]][friend[0]] > 0:  # 서로에게 선물을 준 이력이 있다면
            if giftDict[friend[0]][friend[1]] > giftDict[friend[1]][friend[0]]:  # 첫번째 사람이 더 많이 줬다면
                nextPresent[friend[0]] += 1
            elif giftDict[friend[0]][friend[1]] == giftDict[friend[1]][friend[0]]:  # 둘이 서로 준 선물양이 같다면 선물지수 체크
                if presentPower[friend[0]] > presentPower[friend[1]]:  # 첫번째 사람이 더 선물지수가 높다면
                    nextPresent[friend[0]] += 1
                elif presentPower[friend[1]] > presentPower[friend[0]]:  # 두번째 사람이 더 선물지수가 높다면
                    nextPresent[friend[1]] += 1
            else:  # 두번째 사람이 더 많이 줬다면
                nextPresent[friend[1]] += 1
        else:  # 선물을 준 이력이 없다면 선물지수로만 판단
            if presentPower[friend[0]] > presentPower[friend[1]]:  # 첫번째 사람이 더 선물지수가 높다면
                nextPresent[friend[0]] += 1
            elif presentPower[friend[1]] > presentPower[friend[0]]:  # 두번째 사람이 더 선물지수가 높다면
                nextPresent[friend[1]] += 1

    answer = max(nextPresent.values())  # 값중 가장 큰 값 추출
    return answer