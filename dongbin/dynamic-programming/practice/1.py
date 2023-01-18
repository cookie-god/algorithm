import sys

X = int(sys.stdin.readline().strip())
dp = [0 for _ in range(30001)]  # dp 배열은 i번째 원소에서 연산횟수가 최소가 되는 값들을 저장한 배열

for i in range(2, 30001):
    dp[i] = dp[i - 1] + 1  # 1을 빼는 경우
    if i % 5 == 0:  # 5로 나눌 수 있는 경우
        dp[i] = min(dp[i // 5] + 1, dp[i])  # i를 5로 나눈 값에 + 1의 배열과 현재 1을 뺀 값과 비교
    elif i % 3 == 0:  # 3으로 나눌 수 있는 경우
        dp[i] = min(dp[i // 3] + 1, dp[i])  # i를 3으로 나눈 값에 + 1의 배열과 현재 1을 뺀 값과 비교
    elif i % 2 == 0:  # 2로 나눌 수 있는 경우
        dp[i] = min(dp[i // 2] + 1, dp[i])  # i를 2로 나눈 값에 + 1의 배열과 현재 1을 뺀 값과 비교

print(dp[X])