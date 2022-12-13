import sys

N = int(sys.stdin.readline().strip())
dp = [0 for _ in range(N + 2)]

dp[1] = 0
dp[2] = 1

for i in range(3, N + 1):
    # 3개의 경우 모두 수행을 하기 때문에 if만 사용
    dp[i] = dp[i - 1] + 1  # 1을 빼는 경우
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i // 3] + 1)  # 1을 뺀 경우와 3으로 나누어 떨어지는 것 중에 가장 작은 값을 대입
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i // 2] + 1)  # 1을 뺀 경우와 2로 나누어 떨어지는 것 중에 가장 작은 값을 대입
print(dp[N])
