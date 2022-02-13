import sys

N = int(sys.stdin.readline().strip())

dp = [1 for _ in range(N+1)]
dp[0] = 1 #아무도 배치하지 않는 경우
dp[1] = 3 #N이 1인 경우 없는경우, 한마리씩 배치하는 경우

if N == 1:
    print(dp[1])
else: #2부터 돌리기 위해
    for i in range(2, N+1):
        dp[i] = (2*dp[i-1] + dp[i-2]) % 9901
        #dp[i]에 배치하지 않는 경우 = dp[i-1]
        #dp[i-1]에 배치하지 않는 경우 = dp[i-2]*2 -> dp[i]에는 2개의 위차가 있으므로
        #dp[i], dp[i-1] 모두 배치하는 경우 = dp[i-1]-dp[i-2] -> i-1까지 배치한 경우와 i-2까지 배치한 경우를 빼면 i-1자리에만 배치한 경우가 생기고, i위치는 i-1에 따름
    print(dp[N])


