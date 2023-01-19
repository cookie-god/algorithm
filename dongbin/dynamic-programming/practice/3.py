import sys

N = int(sys.stdin.readline().strip())
dp = [0 for _ in range(N + 1)]  # dp[i]는 가로의 길이가 i인 경우 덮을 수 있는 최대 덮개의 개수
dp[1] = 1
dp[2] = 3

for i in range(3, N + 1):
    dp[i] = (dp[i-1] + dp[i - 2] * 2) % 796796  # 가로 길이가 1 작은 곳에 가로의 길이기 1인 덮개를 넣는 경우 + 가로 길이가 2 작은 곳에 가로의 길이가 2인 덮개를 넣는 경우 -> 2종류니 곱하기 2

print(dp[N])