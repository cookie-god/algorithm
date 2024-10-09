def solution(players, callings):
    answer = []

    dict = {}  # 딕셔너리로 해결
    rank = 0  # 순위는 곧 index
    for player in players:
        dict[player] = rank
        rank += 1

    for calling in callings:
        rank = dict[calling]  # 불린 유저의 순위 가져오기, 순위는 곧 index
        dict[calling] -= 1  # 딕셔너리에서 순위 1 빼기
        dict[players[rank - 1]] += 1  # 불린 유저의 앞의 유저의 딕셔너리 순위 1 더하기
        players[rank - 1], players[rank] = players[rank], players[rank - 1]  # 플레이어 위치 교환

    return players