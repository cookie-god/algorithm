import sys

N, M = map(int, sys.stdin.readline().split())
# array = [[0] * (M+1) for _ in range(N+1)]
# dx = [-2, -1, 1, 2]
# dy = [1, 2, 2, 1]
#
# def isOver(x, y):
#     if x < 1 or x > M or y < 1 or y > N:
#         return False
#     return True
#
# array[N][1] = 1
# firstCheck = 1
# cnt = 1
# cntFlag = False
# flag = False
#
# x = 1
# y = N
#
# while(True):
#     for i in range(4):
#         tmpX = x + dy[i]
#         tmpY = y + dx[i]
#
#         if cnt < 4:
#             firstCheck += 1
#             if isOver(tmpX, tmpY):
#                 x = tmpX
#                 y = tmpY
#                 cnt += 1
#                 break
#         else:
#             if isOver(tmpX, tmpY) == False:
#                 flag = True
#                 break
#             else:
#                 x = tmpX
#                 y = tmpY
#
#     if firstCheck >= 4:
#         cntFlag = True
#
#
#     if cntFlag == True and flag == False:
#         cnt += 4
#
#     if cntFlag == True and flag == True:
#         break
#
# print(cnt)

if N == 1:
    print(1)
elif N == 2:
    print(min(4, (M-1)//2+1))
elif M <= 6:
    print(min(4, M))
else:
    print(M-2)