import sys

T = int(sys.stdin.readline().strip())
result = []
dp = [0]*11
dp[1] = 1
dp[2] = 2
dp[3] = 4
#dp 미리 작성

for i in range(4, 11):
    dp[i] = dp[i-1]+dp[i-2]+dp[i-3] #점화식

for i in range(T):
    N = int(sys.stdin.readline().strip())
    result.append(dp[N]) #정답 배열에 넣음

for i in range(T):
    print(result[i])
