import sys

N = int(sys.stdin.readline().strip())
dp = [[0] * 10 for _ in range(N + 1)]

for i in range(1, 10):
    dp[1][i] = 1

for i in range(2, N + 1):
    for j in range(10):
        if j == 0:
            dp[i][j] = dp[i - 1][1]  # 0앞에 올 수 있는 숫자는 1밖에 존재하지 않음
        elif j == 9:
            dp[i][j] = dp[i - 1][8]  # 9로 시작하는 수는 이전의 8로 시작하는 것에 맨 앞에 9를 붙인 것 뿐이기 때문에
        else:
            dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j + 1]  # 1~8로 시작하는 경우에는 이전의 자리수의 dp 배열에서 가져올 수 있음

print(sum(dp[N]) % 1000000000)