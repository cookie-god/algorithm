import sys

N = int(sys.stdin.readline().strip())
for i in range(N):
    A, B = map(int, sys.stdin.readline().split())
    print('Case #%d: %d' %(i+1, A + B))