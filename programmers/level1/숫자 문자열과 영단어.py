def solution(s):
    answer = ""
    dict = {"zero": 0, "one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8,
            "nine": 9}
    idx = 0
    length = len(s)
    while idx < length:
        if ord("0") <= ord(s[idx]) <= ord("9"):  # 0에서 9사이인 경우
            answer += s[idx]  # 정답 추가
        else:
            check = ""  # 문자열 저장용
            while True:
                check += s[idx]  # 현재 문자 추가
                if check in dict:  # 딕셔너리에 존재하는 경우 정답에 추가후 탈출
                    answer += str(dict[check])
                    break
                idx += 1
        idx += 1

    return int(answer)