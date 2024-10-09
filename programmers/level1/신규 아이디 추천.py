def oneStep(id):  # 대문자를 소문자로
    return id.lower()  # lower 함수를 통해 대문자에서 소문자로 변경


def twoStep(id):  # -, _, . 제외한 모든 문자 제거
    new_id = ""
    for c in id:
        check = ord(c)
        if (ord('a') <= check <= ord('z')) or (ord('0') <= check <= ord('9')) or (
                ord('-') == check or ord('_') == check or ord('.') == check):  # 아스키 코드 값을 통해 비교
            new_id = new_id + c

    return new_id


def threeStep(id):  # 마침표가 여러 개인 경우 하나로만 변경
    new_id = ""
    idx = 0  # 현재 인덱스
    flag = False  # 가장 마지막에 ..이 연속인데 끝난 경우를 확인하기 위해
    while True:
        if idx == len(id):  # 마지막 문자열인
            break
        if id[idx] == ".":  # .인 경우 계속 .이 아닐 때까지 idx 옮겨주기
            new_id += "."  # 일단 추가
            while True:
                idx += 1
                if idx == len(id):  # 마지막 문자열이었다면 종료
                    break
                if id[idx] != ".":  # 다음 문자가 마침표가 아닌 경우 종료
                    break
        else:
            new_id += id[idx]  # 값 추가
            idx += 1  # 인덱스 증가

    return new_id


def fourStep(id):  # 양끝의 . 제거
    if len(id) > 0:  # 길이가 0보다 큰 경우만
        if id[0] == ".":  # 맨 첫번째가 . 인경우
            id = id[1:]
    if len(id) > 0:  # 길이가 0보다 큰 경우만
        if id[-1] == ".":  # 맨 마지막이 . 인경우
            id = id[:-1]
    return id


def fiveStep(id):  # 길이가 0인 애들은 a 리턴
    if len(id) == 0:
        return "a"
    return id


def sixStep(id):  # 길이가 16이상인 경우 15까지 제거
    if len(id) >= 16:
        id = id[:15]
        if id[-1] == ".":  # 아이디 마지막이 .인 경우 마지막 . 제거
            return id[:14]
        return id
    return id


def sevenStep(id):  # 길이가 2자 이하라면 길이가 3이 될때까지 마지막 문자 반복
    if len(id) <= 2:
        c = id[-1]  # 가장 마지막 문자 저장
        count = len(id)
        while True:
            if count == 3:  # 3이 된다면 탈출
                break
            id += c
            count += 1
    return id


def solution(new_id):
    answer = ''
    new_id = oneStep(new_id)
    new_id = twoStep(new_id)
    new_id = threeStep(new_id)
    new_id = fourStep(new_id)
    new_id = fiveStep(new_id)
    new_id = sixStep(new_id)
    new_id = sevenStep(new_id)
    answer = new_id
    return answer