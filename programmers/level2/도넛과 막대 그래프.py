from collections import defaultdict, deque


def solution(edges):
    answer = [0, 0, 0, 0]
    dict = {}
    for a, b in edges:  # 0은 진출, 1은 진입
        if not dict.get(a):
            dict[a] = [0, 0]
        if not dict.get(b):
            dict[b] = [0, 0]

        dict[a][0] += 1
        dict[b][1] += 1

    for key, value in dict.items():
        if value[0] >= 2 and value[1] == 0:  # 진출이 2개 이상이고, 진입이 0인 경우는 생성된 정점
            answer[0] = key
        elif value[0] == 0 and value[1] >= 1:  # 진출이 0개고, 진입이 1개 이상인 경우는 막대모양
            answer[2] += 1
        elif value[0] >= 2 and value[1] >= 2:  # 진출이 2개 이상이고, 진입이 2개 이상인 경우는 8자모양
            answer[3] += 1

    answer[1] = (dict[answer[0]][0] - answer[2] - answer[3])  # 생성된 정점에서 나가는 진출 개수에서 막대 모양, 8자 모양 빼면 도넛 모양 완성
    print(answer)
    return answer