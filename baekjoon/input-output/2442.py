import sys

N = int(sys.stdin.readline().strip())

for i in range(1, N + 1):
    print(' ' * (N - i) + '*' * (i * 2 - 1))