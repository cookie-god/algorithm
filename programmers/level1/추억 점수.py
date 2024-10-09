def solution(name, yearning, photo):
    answer = []
    nameDict = {}

    for i in range(len(name)):
        nameDict[name[i]] = yearning[i]  # 이름별 추억점수 딕셔너리 생성

    for p in photo:
        sum = 0
        for s in p:
            if s in nameDict:  # 딕셔너리에 존재하는 이름이라면
                sum += nameDict[s]
        answer.append(sum)

    return answer