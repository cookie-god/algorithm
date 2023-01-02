import sys

N = int(sys.stdin.readline().strip())
# dp[2][1]은 2자리의 숫자이면서 1로 시작하는 오르막 수의 개수, 첫번째 인덱스는 자리수, 두번째 인덱스는 오르막 수의 첫번째 숫자
dp = [[0] * 10 for _ in range(N + 1)]


for i in range(10):
    dp[1][i] = 1  # 0~9는 1로 초기화

for i in range(2, N + 1):
    for j in range(10):
        dp[i][j] = sum(dp[i-1][j:])  # i번째 자리수의 j로 시작하는 오르막 수는 i-1번째 자리수의 j부터 시작하는 오르막 수들의 총 합

print(sum(dp[N]) % 10007)