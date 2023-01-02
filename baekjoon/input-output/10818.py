import sys

N = int(sys.stdin.readline().strip())
array = list(map(int, sys.stdin.readline().split()))

print('%d %d' %(min(array), max(array)))