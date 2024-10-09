def routeSplit(route):
    location, amount = route.split(" ")  # 위치와 이동 거리 나누기
    return location, int(amount)


def solution(park, routes):
    answer = []
    row = len(park)
    column = len(park[0])
    dx = [0, 0, 1, -1]  # 동, 서, 남, 북
    dy = [1, -1, 0, 0]  # 동, 서, 남, 북

    def move(x, y, index, time):
        nx, ny = x, y
        for i in range(time):
            nx, ny = nx + dx[index], ny + dy[index]
            if nx < 0 or nx >= row or ny < 0 or ny >= column:  # 경계선을 넘으면 원래 x, y값 리턴
                return x, y
            if park[nx][ny] == "X":  # X 만나면 x, y값 리턴
                return x, y

        return nx, ny  # 이동한 값 리턴

    def checkMove(x, y):
        a, b = x, y
        for route in routes:
            location, amount = routeSplit(route)  # 움직여야할 위치와 크기 리턴
            if location == "E":
                a, b = move(a, b, 0, amount)
            elif location == "W":
                a, b = move(a, b, 1, amount)
            elif location == "S":
                a, b = move(a, b, 2, amount)
            else:
                a, b = move(a, b, 3, amount)
        return a, b

    for i in range(row):
        for j in range(column):
            if park[i][j] == "S":  # start면 탐색 시작
                a, b = checkMove(i, j)

    answer.append(a)
    answer.append(b)

    return answer