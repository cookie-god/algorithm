import sys

N, K = map(int, sys.stdin.readline().split())
aArray = list(map(int, sys.stdin.readline().split()))
bArray = list(map(int, sys.stdin.readline().split()))

aArray.sort()
bArray.sort(reverse=True)

for i in range(K):
    if aArray[i] < bArray[i]:
        aArray[i], bArray[i] = bArray[i], aArray[i]
    else:
        break

print(sum(aArray))