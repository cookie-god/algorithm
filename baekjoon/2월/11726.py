import sys

n = int(sys.stdin.readline().strip())
dp = []
dp.append(0) #0일때 경우의 수
dp.append(1) #1일때 경우의 수
dp.append(2) #2일때 경우의 수

for i in range(3, n+1):
    dp.append(dp[i-2]+dp[i-1]) #점화식은 전 인덱스의 값과 전전 인덱스의 값을 더하는 방식 -> 이전 방식에서 타올 하나를 더하는 것이기 때문

print(dp[n]%10007)