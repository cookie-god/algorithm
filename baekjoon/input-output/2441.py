import sys

N = int(sys.stdin.readline().strip())

for i in range(N):
    print(' ' * i + '*' * (N - i))
