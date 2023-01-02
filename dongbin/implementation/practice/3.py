import sys


def checkBorder(x, y):
    if x < 1 or x > 8 or y < 1 or y > 8:
        return False
    return True


inputData = sys.stdin.readline().strip()
row = int(inputData[1])
column = ord(inputData[0]) - ord('a') + 1
locations = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]
count = 0

for location in locations:
    if checkBorder(row + location[0], column + location[1]):
        count += 1

print(count)