import sys

N = int(sys.stdin.readline().strip())
array = []

for _ in range(N):
    array.append(int(sys.stdin.readline().strip()))

array.sort(reverse=True)

for item in array:
    print(item, end=' ')