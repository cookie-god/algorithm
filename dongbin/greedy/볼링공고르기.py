# 내 풀이
# N, K = map(int, input().split())
# data = list(map(int, input().split()))
#
# count = 0
#
# for i in range(0, N) :
#     for j in range(i+1, N) :
#         if data[i] != data[j] :
#             count += 1
#
# print(count)

# 답지
# N, K = map(int, input().split())
# data = list(map(int, input().split()))
#
# array = [0]*11
#
# for x in data :
#     array[x] += 1
#
# result = 0
#
# for i in range(1, K+1) :
#     N -= array[i]
#     result += array[i] * N
#
# print(result)

#2번째
N, K = map(int, input().split())
data = list(map(int, input().split()))

arr = [0]*11

for x in data:
    arr[x] += 1

result = 0

for i in range(1, K+1):
    N -= arr[i]
    result += arr[i] * N #같은 숫자가 여러개인 경우, 여러 경우의 수를 계산하기위해 곱함

print(result)