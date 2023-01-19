import sys

N, M = map(int, sys.stdin.readline().split())
array = []
for i in range(N):
    array.append(int(sys.stdin.readline().strip()))
dp = [10001 for _ in range(M + 1)]
dp[0] = 0

for i in range(N):  # N개의 동전 비교
    for j in range(array[i], M + 1):  # 동전의 단위부터 원하는 금액까지
        if dp[j - array[i]] != 10001:  # 금액에서 동전을 뺐는데, 10001이 아닌 경우에만
            dp[j] = min(dp[j], dp[j - array[i]] + 1)  # 금액에서 동전을 뺀 금액과 기존 금액중 최솟값 결정

if dp[M] == 10001:
    print(-1)
else:
    print(dp[M])
