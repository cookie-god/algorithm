import sys

S = sys.stdin.readline().strip()
array = []
numTotal = 0

for item in S:
    if 48 <= ord(item) <= 57:
        numTotal += int(item)
    else:
        array.append(item)

array.sort()
print(''.join(array)+str(numTotal))