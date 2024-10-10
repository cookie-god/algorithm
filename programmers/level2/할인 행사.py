from collections import defaultdict


def check(wantDict, discountDict):
    count = 0  # 제품 확인
    for key, value in wantDict.items():
        if discountDict[key] != 0:  # 해당 키 값이 존재한다면
            if discountDict[key] == value:  # 키값과 동일한지 체크
                count += 1
            else:  # 키값 존재하지 않으면 실패
                return False
        else:  # 해당 키 값 존재하지 않으면 실패
            return False

    if len(discountDict) != count:  # 키값의 개수와 동일하지 않으면 False
        return False
    else:  # 동일하면 True
        return True


def solution(want, number, discount):
    answer = 0
    wantDict = defaultdict(int)

    for i in range(len(want)):  # 원하는 제품 체크
        wantDict[want[i]] = number[i]

    for i in range(len(discount)):
        discountDict = defaultdict(int)  # 10일동안 구매할 수 있는 제품 딕셔너리
        if i + 10 <= len(discount):  # 길이에 따라 10일동안 구매할 수 있는 제품 딕셔너리 추가
            for j in range(i, i + 10):
                discountDict[discount[j]] += 1
        else:
            for j in range(i, len(discount)):
                discountDict[discount[j]] += 1

        if check(wantDict, discountDict):  # 함수로 체크
            answer += 1  # 날짜 플러스

    return answer