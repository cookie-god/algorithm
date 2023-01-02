import sys

N = sys.stdin.readline().strip()
halfLength = len(N) // 2

leftArr = N[0:halfLength]
rightArr = N[halfLength: len(N)]

leftSum = 0
rightSum = 0

for num in leftArr:
    leftSum += int(num)

for num in rightArr:
    rightSum += int(num)

if leftSum == rightSum:
    print('LUCKY')
else:
    print('READY')