# n = int(input())
# data = list(map(int, input().split()))
#
# data.sort()
# i = 0
# sum = 0
# result = 0
#
# while i < n :
#     sum += 1
#
#     if sum >= data[i] :
#         sum = 0
#         result += 1
#
#     i += 1
#
# print(result)

N = int(input())
data = list(map(int, input().split()))

i = 0
sum = 0
result = 0

while i < N:
    sum += 1

    if sum == data[i]:
        result += 1
        sum = 0

    i += 1

print(sum)