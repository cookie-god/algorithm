import sys

INF = int(1e9)

n = int(sys.stdin.readline().strip())
m = int(sys.stdin.readline().strip())

graph = [[INF] * (n + 1) for _ in range(n + 1)]

# 자기 자신에게 가는 값은 0으로 초기화
for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i == j:
            graph[i][j] = 0

for _ in range(m):
    # A에서 B로 가는 비용은 C
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a][b] = c

# 점화식에 따라 플로이드 워셜 알고리즘을 수행
for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if graph[i][j] == INF:
            print("INFINITY", end=' ')
        else:
            print(graph[i][j], end=' ')
    print()

# 예제
# 4
# 7
# 1 2 4
# 1 4 6
# 2 1 3
# 2 3 7
# 3 1 5
# 3 4 4
# 4 3 2
