from collections import Counter, defaultdict


def solution(X, Y):
    answer = ''
    xCounter = Counter(X)  # 숫자의 개수 파악
    yCounter = Counter(Y)  # 숫자의 개수 파악
    numDict = defaultdict(str)  # 겹치는 숫자 딕셔너리 사용
    flag = False  # 한번도 안겹쳤는지 체크를 위한 플래그값

    print(xCounter)
    for numX, countX in xCounter.items():
        for numY, countY in yCounter.items():
            if numX == numY:  # 두개의 숫자가 같다면 겹침
                flag = True  # 겹쳤다는 플래그 변경
                numDict[numX] = min(countX, countY)  # 둘중 더 작은 값을 딕셔너리에 추가
                break

    if flag == False:  # 겹친 것이 없음
        return "-1"

    numDict = sorted(numDict.items(), key=lambda item: item[0], reverse=True)  # 키 값기준으로 내림차순 정렬
    for num in numDict:
        for i in range(num[1]):
            if answer != "0":  # 이미 기존에 0만 있다면 삽입 X
                answer += num[0]

    return answer