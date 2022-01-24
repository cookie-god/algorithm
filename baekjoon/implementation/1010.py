array = [[0] * 31 for _ in range(31)]

for i in range(31):
    array[1][i] = i #서쪽에 다리 한개인 경우는 동쪽의 개수만큼 다리를 지을 수 있음

for i in range(2, 31):
    for j in range(i, 31):
        for k in range(i-1, j):
            array[i][j] += array[i-1][k] #현재 다리에서 이전에 건넜던 다리를 건넌 경우 합침
T = int(input())

for i in range(3):
    N, M = map(int, input().split())
    print(array[N][M])