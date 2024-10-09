def solution(wallpaper):
    answer = []
    file = []
    row = len(wallpaper)
    column = len(wallpaper[0])
    for i in range(row):
        for j in range(column):
            if wallpaper[i][j] == '#':
                file.append((i, j))

    file.sort(key=lambda x: x[0])
    answer.append(file[0][0])  # lux
    file.sort(key=lambda x: x[1])
    answer.append(file[0][1])  # luy
    file.sort(key=lambda x: -x[0])
    answer.append(file[0][0] + 1)  # rux
    file.sort(key=lambda x: -x[1])
    answer.append(file[0][1] + 1)  # ruy

    return answer