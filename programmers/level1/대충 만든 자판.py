def solution(keymap, targets):
    answer = []
    dict = {}

    for key in keymap:
        for i in range(len(key)):
            if not key[i] in dict:  # 딕셔너리에 데이터 없는 경우
                dict[key[i]] = i + 1
            else:  # 딕셔너리에 데이터 존재하는 경우 최소값으로 변경
                dict[key[i]] = min(dict[key[i]], i + 1)

    for target in targets:
        sum = 0  # 글자수 합계
        for i in range(len(target)):
            if target[i] in dict:  # 글자가 딕셔너리에 존재하는 경우
                sum += dict[target[i]]  # 합계 더해줌
            else:  # 존재하지 않으면 만들 수 없는 문자 바로 리턴
                sum = -1
                break
        answer.append(sum)
    return answer