import sys

array = list(map(str, sys.stdin.readline().strip()))
printArr = []
idx = 0

for item in array:
    if idx == 10:
        print(''.join(printArr))
        idx = 0
        printArr = []
    printArr.append(item)
    idx += 1

print(''.join(printArr))