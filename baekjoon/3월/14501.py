import sys

N = int(sys.stdin.readline().strip())
T, P = [], []
for _ in range(N):
    t, p = map(int, sys.stdin.readline().split())
    T.append(t)
    P.append(p)
dp = [0] * (N+1)

#최대의 값을 가져오기 위해 뒤에서 부터 DP 계산
for i in range(N-1, -1, -1):
    # 현재 인덱스에서 T[i](걸리는 시간)을 더했을 때, N보다 큰 경우
    if i+T[i] > N:
        dp[i] = dp[i+1]
    # 현재 인덱스에서 T[i](걸리는 시간)을 더했을 때, N보다 작은 경우
    else:
        #dp[i]는 이전 dp값과 P[i](받는 금액)+dp[현재 인덱스 + 걸리는 시간](그 이전의 dp값에 접근)중 큰 것을 선택
        dp[i] = max(dp[i+1], P[i]+dp[i+T[i]])
print(dp[0])