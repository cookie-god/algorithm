# import sys
# from itertools import permutations
#
# N, M = map(int, sys.stdin.readline().split())
# array = [i + 1 for i in range(N)]  # 1 ~ N까지의 숫자를 가진 배
# permu = list(permutations(array, M))  # M개 만큼 순열함수 사용
# for item in permu:
#     for num in item:
#         print(num, end=' ')
#     print()
#
# import sys
#
# def backTracking(numList):  # 백트래킹 함수
#     if len(numList) == M:  # 길이가 M과 같다면 탈출
#         array.append(numList)  # 정답 배열에 삽입
#         return
#     else:
#         for i in range(1, N + 1):
#             if i not in numList:
#                 backTracking(numList + [i])  # 리스트 끝 요소에 붙이기
#
#
# N, M = map(int, sys.stdin.readline().split())
# array = []
# for i in range(1, N + 1):  # 1 ~ N까지의 숫자 체크
#     backTracking([i])
#
# for item in array:
#     for num in item:
#         print(num, end = ' ')
#     print()