def rotate_90(list_2d):
    n = len(list_2d)  # 행 길이 계산
    m = len(list_2d[0])  # 열 길이 계산
    new = [[0] * n for _ in range(m)]  # 새 배열 만들기
    for i in range(n):
        for j in range(m):
            new[j][n - i - 1] = list_2d[i][j]  # 90도 회전
    return new


def checkOpen(lock_2d):  # 열쇠를 열 수 있는지 체크하는 함수
    new_length = len(lock_2d) // 3  # 3배 크게 했기 때문에 실제 길이를 구하기 위해 나눠줌
    for i in range(new_length, new_length * 2):
        for j in range(new_length, new_length * 2):
            if lock_2d[i][j] != 1:  # 1이 아니라면 열기 불가능
                return False
    return True


def solution(key, lock):
    answer = False
    keyRow = len(key)  # 키의 길이
    lockRow = len(lock)  # 자물쇠의 길이

    new_lock = [[0] * (lockRow * 3) for _ in range(lockRow * 3)]  # 자물쇠를 3배 크기로 늘림. 이유는 M이 항상 N이하이기 때문임. 자물쇠의 3배 늘린크기에 키가 어디든 들어갈 수 있음

    for i in range(lockRow):
        for j in range(lockRow):
            new_lock[i + lockRow][j + lockRow] = lock[i][j]  # 새로 늘린 자물쇠에 값 대입

    for rotation in range(4):
        key = rotate_90(key)  # 90도 회전하면서 체크
        for i in range(1, lockRow * 2 + 1):  # 자물쇠의 가장 왼쪽 위치부터 체크
            for j in range(1, lockRow * 2 + 1):  # 자물쇠의 가장 위쪽 위치부터 체크
                for k in range(keyRow):  # 키의 가장 위쪽부터 체크
                    for l in range(keyRow):  # 키의 가장 왼쪽부터 체크
                        new_lock[i + k][j + l] += key[k][l]  # 키값을 더해줌

                if checkOpen(new_lock):  # 열 수 있는지 체크
                    return True

                for m in range(keyRow):  # 열 수 없다면 자물쇠 값들 롤백
                    for n in range(keyRow):
                        new_lock[i + m][j + n] -= key[m][n]

    return answer

# def rotate_90(list_2d):
#     n = len(list_2d) # 행 길이 계산
#     m = len(list_2d[0]) # 열 길이 계산
#     new = [[0] * n for _ in range(m)]
#     for i in range(n):
#         for j in range(m):
#             new[j][n - i - 1] = list_2d[i][j]  # 90도를 회전시키는 로직
#     return new
#
# def checkBorder(x, y, lockRaw, lockColumn):  # 경계선을 넘어갔는지 체크하는 함수
#     if x < 0 or x >= lockRaw or y < 0 or y >= lockColumn:
#         return False
#     return True
#
# def checkOpen(lock_2d):  # 열 수 있는지 체크하는 함수
#     for i in range(len(lock_2d)):
#         for j in range(len(lock_2d[0])):
#             if lock_2d[i][j] == 0:  # 0이 하나라도 존재하면 열 수 없음
#                 return False
#     return True
#
# def solution(key, lock):
#     answer = False
#     # 각각의 Key와 Lock 길이 계산
#     keyRow = len(key)
#     keyColumn = len(key[0])
#     lockRow  = len(lock)
#     lockColumn = len(lock[0])
#
#     for i in range(4):  # 4번 회전 가능
#         key = rotate_90(key)  # 90도 회전
#         for j in range(lockRow):  # Lock 행에 대한 for문
#             for k in range(lockColumn):  # Lock 열에 대한 for문
#                 for l in range(keyRow):  # Key 행에 대한 for문
#                     for m in range(keyColumn):  # Key 열에 대한 for문
#                         if checkBorder(l + j, m + k, lockRow, lockColumn):  # 경계값 넘어가는지 체크
#                             lock[l + j][m + k] += key[l][m]  # Lock에 key의 값을 더해줌
#                 if checkOpen(lock):  # 열 수 있다면 종료
#                     answer = True
#                     return answer
#                 # 열 수 없다면 롤백
#                 for n in range(keyRow):
#                     for o in range(keyColumn):
#                         if checkBorder(j + n, m + o, lockRow, lockColumn):
#                             lock[j + n][m + o] -= key[n][o]  # Lock 다시 롤백
#
#     return answer