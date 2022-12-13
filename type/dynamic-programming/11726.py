import sys

N = int(sys.stdin.readline().strip())
dp = [0 for _ in range(N + 2)]

dp[1] = 1
dp[2] = 2

for i in range(3, N + 2):
    dp[i] = dp[i - 1] + dp[i - 2]  # dp[i-1]배열에 1*2 타일, dp[i-2]배열에 2*1 타일

print(dp[N] % 10007)

