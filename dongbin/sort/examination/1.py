import sys

N = int(sys.stdin.readline().strip())
array = []
for _ in range(N):
    name, korean, english, math = map(str, sys.stdin.readline().split())
    array.append((name, int(korean), int(english), int(math)))

array.sort(key=lambda x:(-x[1], x[2], -x[3], x[0]))
for item in array:
    print(item[0])