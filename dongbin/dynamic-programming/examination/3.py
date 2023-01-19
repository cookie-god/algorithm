import sys

N = int(sys.stdin.readline().strip())
array = []
for _ in range(N):
    array.append(list(map(int, sys.stdin.readline().split())))
dp = [0 for _ in range(N + 1)]

# Top Down 방식으로 진행
for i in range(N - 1, -1, -1):
    time = array[i][0] + i  # 상담이 끝나는 기간
    if time <= N:  # N보다 작은 경우에만 상담이 가능
        dp[i] = max(array[i][1] + dp[time], dp[i + 1])  # 상담을 하는 경우와 그날 상담을 안하는 경우
    else:
        dp[i] = dp[i + 1]  # 상담을 못하기 때문에 안하는 경우로 대입

print(dp[0])