import sys

N = int(sys.stdin.readline().strip())

for i in range(1, N + 1):
    print(' ' * (N - i), end='')
    if i == N:
        print('*' * (i * 2 - 1), end='')
    else:
        for j in range(i * 2 -1):
            if j == 0 or j == i * 2 - 2:
                print('*', end='')
            else:
                print(' ', end='')
    print()