import sys

T = int(sys.stdin.readline().strip())

dp = [0 for _ in range(11)]
dp[1] = 1
dp[2] = 2
dp[3] = 4

for i in range(4, 11):
    dp[i] = dp[i - 1] + dp[i - 2] + dp[i - 3]
    # 각 dp배열 원소에서 1, 2, 3을 더하면 되는 원소의 개수 ex) dp[4]는 dp[3]에 1을 더한 개수,
    # dp[2]에 2를 더한 개수, dp[1]에 3을 더한 개수를 합치면 됨

for _ in range(T):
    n = int(sys.stdin.readline().strip())
    print(dp[n])