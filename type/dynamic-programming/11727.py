import sys

N = int(sys.stdin.readline().strip())
dp = [0 for _ in range(N + 2)]

dp[1] = 1
dp[2] = 3

for i in range(3, N + 2):
    dp[i] = dp[i - 1] + 2 * dp[i - 2]  # 뒤에 길이가 1인 타일이 붙는 경우, 2종류의 길이가 2인 타일이 붙는 경우

print(dp[N] % 10007)

