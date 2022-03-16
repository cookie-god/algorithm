import sys

N = int(sys.stdin.readline().strip())

array = []

for i in range(N):
    [x, y] = map(int, sys.stdin.readline().split())
    array.append([x, y])

array = sorted(array) #sort해줌

for i in range(N):
    print(array[i][0], array[i][1]) #x, y출력