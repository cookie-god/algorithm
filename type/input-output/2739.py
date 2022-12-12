import sys

N = int(sys.stdin.readline().strip())
for i in range(1, 10):
    print('%d * %d = %d' %(N, i, N * i))