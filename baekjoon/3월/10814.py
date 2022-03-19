import sys

N = int(sys.stdin.readline().strip())

array = []
for i in range(N):
    x, y = sys.stdin.readline().split()
    x = int(x)
    array.append((x, y, i)) #들어온 순서도 같이 기록

array.sort(key=lambda x:(x[0], x[2])) #나이 기준으로 먼저 하고, 들어온 순서대로 정렬
for i in range(N):
    print("%d %s" %(array[i][0], array[i][1]))