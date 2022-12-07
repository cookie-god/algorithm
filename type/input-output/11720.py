import sys

N = int(sys.stdin.readline().strip())
num = list(map(int, sys.stdin.readline().strip()))
sum = 0
for i in range(N):
    sum += num[i]
print(sum)