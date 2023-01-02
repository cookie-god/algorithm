import sys


def checkBorder(x, y):
    if x < 1 or x > N or y < 1 or y > N:
        return False
    return True


N = int(sys.stdin.readline().strip())
plan = list(map(str, sys.stdin.readline().split()))
array = [[0] * (N + 1) for _ in range(N + 1)]
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
x, y = 1, 1

for location in plan:
    if location == 'R':
        if checkBorder(x + dx[0], y + dy[0]):
            x += dx[0]
            y += dy[0]
    elif location == 'L':
        if checkBorder(x + dx[1], y + dy[1]):
            x += dx[1]
            y += dy[1]
    elif location == 'D':
        if checkBorder(x + dx[2], y + dy[2]):
            x += dx[2]
            y += dy[2]
    elif location == 'U':
        if checkBorder(x + dx[3], y + dy[3]):
            x += dx[3]
            y += dy[3]

print(x, y)