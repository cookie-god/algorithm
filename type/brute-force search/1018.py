import sys

def check(x, y):
    firstCase = 0
    secondCase = 0

    # wbwb, bwbw 케이스 둘다 구함
    for i in range(x, x + 8):
        for j in range(y, y + 8):
            if i % 2 == 0 and j % 2 == 0:
                if array[i][j] != 'W':
                    firstCase += 1
            elif i % 2 == 0 and j % 2 == 1:
                if array[i][j] != 'B':
                    firstCase += 1
            elif i % 2 == 1 and j % 2 == 0:
                if array[i][j] != 'B':
                    firstCase += 1
            elif i % 2 == 1 and j % 2 == 1:
                if array[i][j] != 'W':
                    firstCase += 1

    for i in range(x, x + 8):
        for j in range(y, y + 8):
            if i % 2 == 0 and j % 2 == 0:
                if array[i][j] != 'B':
                    secondCase += 1
            elif i % 2 == 0 and j % 2 == 1:
                if array[i][j] != 'W':
                    secondCase += 1
            elif i % 2 == 1 and j % 2 == 0:
                if array[i][j] != 'W':
                    secondCase += 1
            elif i % 2 == 1 and j % 2 == 1:
                if array[i][j] != 'B':
                    secondCase += 1

    return min(firstCase, secondCase)


N, M = map(int, sys.stdin.readline().split())
array = []
result = 32

for i in range(N):
    array.append(list(map(str, sys.stdin.readline().strip())))

for i in range(N):
    for j in range(M):
        if N >= i + 8 and M >= j + 8:
            result = min(result, check(i ,j))

print(result)