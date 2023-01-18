import sys
import math

M, N = map(int, sys.stdin.readline().split())
array = [True for _ in range(N + 1)]
array[1] = False
for i in range(2, int(math.sqrt(N)) + 1):
    if array[i]:
        j = 2
        while i * j <= N:
            array[i * j] = False
            j += 1

for i in range(M, N + 1):
    if array[i]:
        print(i)