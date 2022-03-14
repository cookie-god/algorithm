import sys

n = int(sys.stdin.readline().strip())

dp = []
dp.append(0)
dp.append(1)
dp.append(3)

for i in range(3, n+1):
    dp.append(dp[i-1]+dp[i-2]*2) #점화식은 전 인덱스의 값과 전전 인덱스의 값의 2배를 더하는 방식 -> 전전꺼의 방식에서 이어서 붙인 것이기 때문에 2배 더한 것과 같음

print(dp[n]%10007)