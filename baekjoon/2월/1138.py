import sys

N = int(sys.stdin.readline().strip())
array = list(map(int, sys.stdin.readline().split()))
result = [0]*N

# 내 로직
# for i in range(N):
#     if result[array[i]] == 0:
#         result[array[i]] = i+1
#     else:
#         for j in range(array[i], N):
#             if result[j] == 0:
#                 if array[i] > 1 :
#                     result[j + array[i] - 1] = i+1
#                 else:
#                     result[j] = i+1
#                 break

for i in range(N):
    cnt = 0 #추후에 위치 지정을 위한 변수
    for j in range(N):
        if cnt == array[i] and result[j] == 0: #result[j]가 0이고 array[i]와 cnt가 같지 않다면 적합한 위치가 아님
            result[j] = i + 1
            break
        elif(result[j] == 0): #result[j]가 0이지만 위에서 이미 적합하지 않았으므로 cnt 늘려줌
            cnt += 1

for i in range(N):
    print(result[i], end=" ")