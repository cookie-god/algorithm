import sys

N = int(sys.stdin.readline().strip())
array = []
for _ in range(N):
    name, score = map(str, sys.stdin.readline().split())
    array.append((name, int(score)))
array.sort(key=lambda x:x[0])
for item in array:
    print(item[0], end = ' ')