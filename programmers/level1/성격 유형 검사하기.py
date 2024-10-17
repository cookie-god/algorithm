def getAnswerDictIdx(character):  # 정답 딕셔너리의 인덱스와 유형에 따라 덧셈 뺄셈 유무 리턴
    if character == "R" or character == "T":
        if character == "T":
            return 1, "-"
        return 1, "+"
    elif character == "C" or character == "F":
        if character == "F":
            return 2, "-"
        return 2, "+"
    elif character == "J" or character == "M":
        if character == "M":
            return 3, "-"
        return 3, "+"
    else:
        if character == "N":
            return 4, "-"
        return 4, "+"


def solution(survey, choices):
    answer = ''

    answerDict = {}  # 각 유형별 데이터 딕셔너리 셋팅
    for i in range(4):
        answerDict[i + 1] = 0  # 1 -> (R, T), 2 -> (C, F), 3 -> (J, M), 4 -> (A, N)

    for i in range(len(survey)):
        if choices[i] > 4:  # 4보다 큰 경우는 survey[i][1]의 점수 오름
            idx, operation = getAnswerDictIdx(survey[i][1])  # 딕셔너리 인덱스와 더하기 빼기 유무 체크
            if operation == "+":  # R, C, J, A인 경우
                answerDict[idx] += choices[i] - 4
            else:  # T, F, M, M인 경우
                answerDict[idx] -= choices[i] - 4
        elif choices[i] < 4:  # 4보다 작은 경우는 survey[i][0]의 점수 오름
            idx, operation = getAnswerDictIdx(survey[i][0])  # 딕셔너리 인덱스와 더하기 빼기 유무 체크
            if operation == "+":  # R, C, J, A인 경우
                answerDict[idx] += 4 - choices[i]
            else:  # T, F, M, M인 경우
                answerDict[idx] -= 4 - choices[i]

    for key, value in answerDict.items():
        if key == 1:  # R, T에 대해서
            if value >= 0:
                answer += "R"
            elif value < 0:
                answer += "T"
        elif key == 2:  # C, F에 대해서
            if value >= 0:
                answer += "C"
            elif value < 0:
                answer += "F"
        elif key == 3:  # J, M에 대해서
            if value >= 0:
                answer += "J"
            elif value < 0:
                answer += "M"
        else:  # A, N에 대해서
            if value >= 0:
                answer += "A"
            elif value < 0:
                answer += "N"

    return answer