import math


def solution(n, k):
    answer = []
    number = [i for i in range(1, n + 1)]  # 사용 가능한 숫자 셋팅

    while True:
        if len(number) == 0:
            break
        count = math.factorial(n - 1)  # 현재 위치에서 가능한 숫자의 개수
        idx = (k - 1) // count  # number 숫자 내의 인덱스
        answer.append(number.pop(idx))  # answer에 삽입
        k = k % count  # 현재 자리수 이동
        n -= 1  # n 줄여서 다음 자리로 이동

    return answer

# def dfs(n, arr, location):
#     global flag, answer, checkIndex

#     if location == checkIndex:
#         return

#     if len(arr) == n:
#         checkIndex += 1

#     if location == checkIndex:
#         answer = arr.copy()
#         return

#     for i in range(1, n + 1):
#         if i not in arr:
#             arr.append(i)
#             dfs(n, arr, location)
#             arr.pop()


# def solution(n, k):
#     global flag, answer, checkIndex
#     flag = False
#     answer = []
#     checkIndex = 0
#     arr = []
#     dfs(n, arr, k)

#     return answer