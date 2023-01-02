import sys

N = int(sys.stdin.readline().strip())
array = list(map(int, sys.stdin.readline().split()))
dp = [1 for _ in range(N)]

for i in range(1, N):
    for j in range(i):  # i 인덱스 안에서 비교하는 이유는 j부터 i까지 비교하면서 dp[i]를 확실히 정하기 위해서
        if array[i] > array[j]:  # array[i]가 array[j]보다 큰 경우 부분 수열이기 때문에 dp[i]를 최신화 한다
            dp[i] = max(dp[i], dp[j] + 1)  # dp[j]는 이미 j 인덱스까지 이미 확정된 오름차순의 숫자의 수이므로 여기에 1을 더한 것과 기존의 dp[i]와 비교한다.

print(max(dp))


# import sys
#
# N = int(sys.stdin.readline().strip())
# array = list(map(int, sys.stdin.readline().split()))
# array.insert(0, 0)
#
# dp = [[0] * (N + 1) for _ in range(N + 1)]
#
# for i in range(1, N + 1):
#     dp[i][i] = 1
#
# idx = 0
# for i in range(1, N + 1):
#     idx = i
#     for j in range(i + 1, N + 1):
#         if array[idx] < array[j]:
#             dp[i][j] = dp[i][idx] + 1
#             idx = j
#         else:
#             dp[i][j] = dp[i][idx]
#
#
# result = 0
# for i in range(1, N + 1):
#     for j in range(1, N + 1):
#         if result <= dp[i][j]:
#             result = dp[i][j]
#
# print(result)
