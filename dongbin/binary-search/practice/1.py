import sys

def binarySearch(start, end, target):
    mid = (start + end) // 2

    if start > end:
        return 'no'
    elif nArray[mid] == target:
        return 'yes'
    elif nArray[mid] < target:
        return binarySearch(mid + 1, end, target)
    else:
        return binarySearch(start, mid - 1, target)


N = int(sys.stdin.readline().strip())
nArray = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline().strip())
mArray = list(map(int, sys.stdin.readline().split()))

nArray.sort()
mid = len(nArray) // 2

answer = []
for item in mArray:
    answer.append(binarySearch(0, len(nArray) - 1, item))

for item in answer:
    print(item, end = ' ')