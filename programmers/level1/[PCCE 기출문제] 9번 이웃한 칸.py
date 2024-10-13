def solution(board, h, w):
    answer = 0
    n = len(board)  # 1번 순서
    count = 0  # 2번 순서
    dh = [0, 1, -1, 0]  # 3번 순서
    dw = [1, 0, 0, -1]  # 3번 순서

    for i in range(4):  # 4번 순서
        h_check, w_check = h + dh[i], w + dw[i]  # 4-1번 순서
        if 0 <= h_check < n and 0 <= w_check < n:  # 4-2번 수서
            if board[h][w] == board[h_check][w_check]:  # 4-2-a번 순서
                count += 1

    return count