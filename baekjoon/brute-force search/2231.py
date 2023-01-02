import sys

N = int(sys.stdin.readline())
i = 1
tmp = 0
result = 0
divideSum = 0
while i < N:
    divideSum = i
    tmp = i
    while tmp != 0:
        divideSum += tmp % 10
        tmp //= 10

    if divideSum == N:
        result = i
        break
    i += 1

print(result)
