def solution(data, ext, val_ext, sort_by):
    answer = [[]]

    if ext == "code":
        data = list(filter(lambda x: x[0] < val_ext, data))  # x는 1차 리스트니 거기서 첫번째 원소만 체크
    elif ext == "date":
        data = list(filter(lambda x: x[1] < val_ext, data))  # x는 1차 리스트니 거기서 두번째 원소만 체크
    elif ext == "maximum":
        data = list(filter(lambda x: x[2] < val_ext, data))  # x는 1차 리스트니 거기서 세번째 원소만 체크
    else:
        data = list(filter(lambda x: x[3] < val_ext, data))  # x는 1차 리스트니 거기서 네번째 원소만 체크

    if sort_by == "code":
        data.sort(key=lambda x: x[0])  # 첫번째 원소에 대해서 오름 차순 정렬
    elif sort_by == "date":
        data.sort(key=lambda x: x[1])  # 두번째 원소에 대해서 오름 차순 정렬
    elif sort_by == "maximum":
        data.sort(key=lambda x: x[2])  # 세번째 원소에 대해서 오름 차순 정렬
    else:
        data.sort(key=lambda x: x[3])  # 네번째 원소에 대해서 오름 차순 정렬

    answer = data
    return answer