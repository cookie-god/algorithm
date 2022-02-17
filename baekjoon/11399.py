import sys

N = int(sys.stdin.readline())

array = list(map(int, sys.stdin.readline().split()))
array.sort() #정렬

result = 0
total = 0
for num in array:
    total += num #누적 계산
    result += total #결과값 누적 계산
print(result)