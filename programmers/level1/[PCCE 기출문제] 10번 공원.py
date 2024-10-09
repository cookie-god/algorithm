def solution(mats, park):
    answer = 0
    result = 0  # x, y 좌표에서 돗자리 깔 수 있는 최대 길이
    row = len(park)  # 세로길이
    column = len(park[0])  # 가로길이
    mats.sort(reverse=True)  # 역순 정렬

    def checkPicnic(x, y):
        for data in mats:  # 돗자리 크기순서대로 체크
            check = 1  # check 1로 초기화 1이면 돗자리 깔 수 있는 영역
            for i in range(x, x + data):  # 돗자리 크기만큼 세로 배열 영역 더 체크
                if i >= row:  # index out 체크
                    check = 0  # check 0으로 변경 -> 다음 돗자리 바로 체크 가능
                    break  # 세로 길이 체크하다 나옴
                for j in range(y, y + data):  # 돗자리 크기만큼 가로 배열 더 체크
                    if j >= column:  # index out 체크
                        check = 0  # check 0으로 변경 -> 다음 돗자리 바로 체크 가능
                        break  # 길이 체크하다 나옴
                    if park[i][j] != "-1":  # 이미 돗자리 깔려 있는 경우 체크
                        check = 0  # check 0으로 변경 -> 다음 돗자리 바로 체크 가능
                        break  # 가로, 세로 길이 모두 부합했지만 돗자리 이미 깔려 있어서 다음 돗자리 체크
                if check == 0:  # 해당 돗자리는 못까는 경우이므로 다음 작은 돗자리 체크
                    break  # 다음 돗자리 조회 for문으로 이동
            if check == 1:  # 돗자리 크기대로 정렬을 했기 때문에 최대값 리턴
                return data
        return 0  # 돗자리를 아예 못깐다면 0 리턴

    for i in range(row):
        for j in range(column):
            if park[i][j] == "-1":  # -1인 경우에만 함수 체크
                result = checkPicnic(i, j)  # 결과값 리턴
                if result != 0:  # 0이 아닌 경우에만 최대값 계산
                    answer = max(answer, result)

    if answer == 0:  # 0이면 돗자리를 아예 못까는 경우
        answer = -1
    return answer