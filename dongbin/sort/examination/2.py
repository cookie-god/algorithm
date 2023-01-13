# 시간 초과

# import sys
#
# N = int(sys.stdin.readline().strip())
# array = [0 for _ in range(100001)]
# indexList = list(map(int, sys.stdin.readline().split()))
# maxIndex = 0
# for i in range(N):
#     if maxIndex < indexList[i]:
#         maxIndex = indexList[i]
#     array[indexList[i]] += 1
#
# result = 100000000
# index = 1
#
# for i in range(1, maxIndex + 1):
#     distance = 0
#     for j in range(1, maxIndex + 1):
#         if array[j] != 0:
#             distance += (abs(i - j)) * array[j]
#
#     if result > distance:
#         index = i
#         result = distance
#
# print(index)


import sys

N = int(sys.stdin.readline().strip())
array = list(map(int, sys.stdin.readline().split()))
array.sort()
print(array[(N - 1) // 2])
