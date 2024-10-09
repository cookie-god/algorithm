def makeSecond(time):
    min, second = time.split(":")
    return int(min) * 60 + int(second)


def makeTime(second):
    min_str = second // 60
    second_str = second % 60

    if min_str < 10:
        min_str = "0" + str(min_str)
    else:
        min_str = str(min_str)

    if second_str < 10:
        second_str = "0" + str(second_str)
    else:
        second_str = str(second_str)

    return min_str + ":" + second_str


def checkOpening(pos, op_start, op_end):  # 매번 체크 해야함
    if op_start <= pos <= op_end:
        return True
    return False


def solution(video_len, pos, op_start, op_end, commands):
    answer = ''
    video_len = makeSecond(video_len)
    pos = makeSecond(pos)
    op_start = makeSecond(op_start)
    op_end = makeSecond(op_end)

    if checkOpening(pos, op_start, op_end):  # 시작하기 전에 위치 체크
        pos = op_end

    for command in commands:
        if command == "next":  # next면 10 추가
            if pos + 10 > video_len:
                pos = video_len
            else:
                pos = pos + 10

        if command == "prev":  # prev면 10 빼기
            if pos - 10 < 0:
                pos = 0
            else:
                pos = pos - 10

        if checkOpening(pos, op_start, op_end):  # 이동 후 오프닝 시간에 위치한다면 끝나는 순간으로 이동
            pos = op_end

    answer = makeTime(pos)
    return answer
