def checkBorder(w_width, w_height, b_width, b_height):  # 지갑에 지폐를 넣을 수 있는지 체크
    if w_width >= b_width and w_height >= b_height:  # 지갑의 가로길이 보다 지폐의 가로길이가 더 짧거나 같고 지갑의 세로길이보다 지폐의 세로길이가 더 짧은 경우
        return True
    elif w_width >= b_height and w_height >= b_width:  # 지갑의 가로길이 보다 지폐의 세로길이가 더 짧거나 같고 지갑의 세로길이보다 지폐의 가로길이가 더 짧은 경우
        return True
    else:  # 그 외에는 False
        return False


def changeBillSize(b_width, b_height):  # 접는 함수
    if b_width > b_height:  # 가로가 더 긴 경우 가로를 나눔
        return b_width // 2, b_height
    else:  # 세로가 더 길거나 같은 경우 세로를 나눔
        return b_width, b_height // 2


def solution(wallet, bill):
    answer = 0  # 접은 횟수
    w_width = wallet[0]
    w_height = wallet[1]
    b_width = bill[0]
    b_height = bill[1]

    while (True):
        if checkBorder(w_width, w_height, b_width, b_height):  # 넣을 수 있는지 체크
            break
        else:
            b_width, b_height = changeBillSize(b_width, b_height)  # 접기 진행
            answer = answer + 1  # 접은 횟수 추가

    return answer