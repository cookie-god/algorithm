# 2개가 필요한 이유 0110
# arr = input()
#
# findNum = '0'
# beforeNum = -1
# if arr.count('0') > arr.count('1') :
#     findNum = '1'
#
# cnt = 0
# count = 0
# length = len(arr)
#
# for i in arr :
#     if i == findNum :
#         if i == arr[length-1] :
#             cnt += 1
#         else :
#             beforeNum = int(i)
#     else :
#         if beforeNum != -1 :
#             beforeNum = -1
#             cnt += 1
#
#     count += 1
#
# print(cnt)

# arr = input()
#
# count0 = 0
# count1 = 0
#
# if arr[0] == '1':
#     count0 = 1
# else:
#     count1 = 1
#
# for i in range(len(arr)-1):
#     if arr[i] != arr[i+1]:
#         if arr[i+1] == '1':
#             count0 += 1
#         else:
#             count1 += 1
#
# print(min(count0, count1))

arr = input()

count0 = 0
count1 = 0

if arr[0] == '1':
    count0 = 1
else:
    count1 = 1

for i in range(len(arr)-1):
    if arr[i] != arr[i+1]:
        if arr[i+1] == '1':
            count0 += 1
        else:
            count1 += 1

print(min(count0, count1))
#둘중 최소값을 출력하기