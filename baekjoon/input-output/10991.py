import sys

N = int(sys.stdin.readline().strip())

for i in range(1, N + 1):
    print(' ' * (N - i), end='')
    for j in range(i * 2 -1):
        if j % 2 == 0:
            print('*', end='')
        else:
            print(' ', end='')
    print()