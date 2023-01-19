import sys

N = int(sys.stdin.readline().strip())
array = list(map(int, sys.stdin.readline().split()))
dp = [0 for _ in range(N + 1)]  # dp[i]는 i번째까지 가장 많은 식량값
array.insert(0, 0)
dp[1] = array[1]
dp[2] = max(array[1], array[2])

for i in range(3, N + 1):
    dp[i] = max(dp[i - 1], dp[i - 2] + array[i])  # 이번 식량을 선택하지 않는 것이 좋은지, 이번 식량을 선택하는 것이 좋은지 비교
print(dp[N])