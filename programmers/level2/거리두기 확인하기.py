def checkBorder(x, y):
    if 0 <= x < 5 and 0 <= y < 5:
        return True
    return False


def checkAdjacent(place):
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    for i in range(5):
        for j in range(5):
            if place[i][j] == "P":  # P인 경우 4방향 체크
                locations = []  # P에 맨해튼 거리가 2이하인 좌표 저장용
                for k in range(4):  # 4방향 이동
                    x = i + dx[k]
                    y = j + dy[k]
                    if checkBorder(x, y):  # 경계선 체크
                        if place[x][y] != "X":  # X가 아닌 경우 4방향에 대한 데이터 locations에 삽입
                            locations.append((x, y))  # 현재 위치삽입
                            if checkBorder(x - 1, y):  # 왼쪽
                                locations.append((x - 1, y))
                            if checkBorder(x + 1, y):  # 오른쪽
                                locations.append((x + 1, y))
                            if checkBorder(x, y - 1):  # 위쪽
                                locations.append((x, y - 1))
                            if checkBorder(x, y + 1):  # 아래쪽
                                locations.append((x, y + 1))
                        elif place[x][y] == "P":  # P면 바로 0리턴
                            return 0
                locations = list(set(locations))  # 중복값 제거
                if (i, j) in locations:  # 만약 초기 P값이 locations 내에 존재한다면 제거
                    locations.remove((i, j))

                for location in locations:
                    if place[location[0]][location[1]] == "P":  # location에 P인 데이터가 존재한다면
                        return 0

    return 1


def solution(places):
    answer = []
    for place in places:
        answer.append(checkAdjacent(place))

    return answer