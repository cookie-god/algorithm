import sys

N = int(sys.stdin.readline().strip())

for i in range(N):
    for j in range(i+1):
        print('*', end='')
    print()