import sys
import time

def binarySearch(start, end):
  global minIdx, maxIdx

  print(start, end)
  time.sleep(3)
  if start >= end:
    return

  mid = (start + end) // 2
  if array[mid] <= x:
    minIdx = min(minIdx, mid)
    maxIdx = max(maxIdx, mid)
    print('down')
    binarySearch(start, mid - 1)
    print('up')
    binarySearch(mid, end)
  else:
    binarySearch(start, mid - 1)


N, x = map(int, sys.stdin.readline().split())
array = list(map(int, sys.stdin.readline().split()))
minIdx = N - 1
maxIdx = 0

binarySearch(0, N - 1)
print(minIdx, maxIdx)