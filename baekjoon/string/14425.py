import sys

N, M = map(int, sys.stdin.readline().split())
S = []
array = []

for _ in range(N):
    S.append(sys.stdin.readline().strip())

for _ in range(M):
    array.append(sys.stdin.readline().strip())

result = 0

for item in array:
    if item in S:
        result += 1
print(result)