import sys

N = int(sys.stdin.readline().strip())
array = []

minus = 0  # -1의 종이수가 저장되는 변수
zero = 0  # 0의 종이수가 저장되는 변수
plus = 0  # 1의 종이수가 저장되는 변수

for _ in range(N):
    array.append(list(map(int, sys.stdin.readline().split())))


def dfs(x, y, n):
    global minus, zero, plus
    criteria = array[x][y]  # 숫자 기준

    for i in range(x, x + n):
        for j in range(y, y + n):
            if array[i][j] != criteria:  # 기준과 다른 경우 종이를 나눠야함
                for k in range(3):  # 9개로 나누기 위해 3
                    for l in range(3):  # 9개로 나누기 위해 3
                        dfs(x + k * n // 3, y + l * n // 3, n // 3)
                return

    # 기준 체크
    if criteria == -1:
        minus += 1
    elif criteria == 0:
        zero += 1
    elif criteria == 1:
        plus += 1


dfs(0, 0, N)

print(minus)
print(zero)
print(plus)