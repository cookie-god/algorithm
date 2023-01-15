# import sys
# from itertools import permutations
#
# N, M = map(int, sys.stdin.readline().split())
# array = [i + 1 for i in range(N)]
# combi = list(permutations(array, M))
# for item in combi:
#     for num in item:
#         print(num, end=' ')
#     print()

# import sys
#
# def backTracking(numList):
#     if len(numList) == M:
#         array.append(numList)
#         return
#     else:
#         for i in range(1, N + 1):
#             if i not in numList:
#                 backTracking(numList + [i])
#
#
# N, M = map(int, sys.stdin.readline().split())
# array = []
# for i in range(1, N + 1):
#     backTracking([i])
#
# for item in array:
#     for num in item:
#         print(num, end = ' ')
#     print()