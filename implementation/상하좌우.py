def checkMove(x, y):
    if x < 1 or x > N or y < 1 or y > N:
        return False
    return True

N = int(input())
moves = input().split()

x = 1
y = 1

for move in moves:
    if move == 'R':
        if checkMove(x+1, y):
            x += 1

    elif move == 'L':
        if checkMove(x+1, y):
            x -= 1

    elif move == 'U':
        if checkMove(x, y-1):
            y -= 1

    elif move == 'D':
        if checkMove(x, y+1):
            y += 1

print(y, x)


