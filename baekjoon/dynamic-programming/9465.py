import sys

T = int(sys.stdin.readline().strip())

for i in range(T):
    n = int(sys.stdin.readline().strip())
    dp = [list(map(int, sys.stdin.readline().split())) for _ in range(2)]

    if n > 1:
        dp[0][1] += dp[1][0]  # 맨 처음 대각선에 있는 점수 더하기
        dp[1][1] += dp[0][0]  # 맨 처음 대각선에 있는 점수 더하기

        for j in range(2, n):
            dp[0][j] += max(dp[1][j - 2], dp[1][j - 1])  # 왼쪽 대각선에 있는 것과 왼쪽 대각선 옆에 있는 것이랑 비교
            dp[1][j] += max(dp[0][j - 2], dp[0][j - 1])  # 왼쪽 대각선에 있는 것과 왼쪽 대각선 옆에 있는 것이랑 비교

    print(max(dp[0][n - 1], dp[1][n - 1]))