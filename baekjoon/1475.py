import sys
import math

arr = sys.stdin.readline().strip()
numCount = [0]*10

for alpha in arr:
    if alpha == '9' or alpha =='6':
        numCount[int(alpha)] += 0.5
    else:
        numCount[int(alpha)] += 1

numCount[6] += numCount[9]
numCount[9] = numCount[6]


print(math.ceil(max(numCount)))