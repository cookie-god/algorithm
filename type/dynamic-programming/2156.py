import sys

n = int(sys.stdin.readline().strip())
arr = [0]
dp = [0 for _ in range(n + 1)]  # dp[i]는 i번째 포도주 잔에서 최대로 포도주를 먹은 양을 담는 배열
for _ in range(n):
    arr.append(int(sys.stdin.readline().strip()))

dp[1] = arr[1]

if n >= 2:  # 1이상부터 되므로
    dp[2] = arr[1] + arr[2]

for i in range(3, n + 1):
    dp[i] = max(arr[i] + arr[i-1] + dp[i - 3], arr[i] + dp[i - 2], dp[i - 1])
    #  현재 포도주양, 전 포도주양, 처음부터 전전전 포도주까지 먹은 양중에 가장 많이 먹을 수 있는 방법으로 먹은 포도주(dp[전전전])를 먹는 경우, 즉 전전 포도주를 먹지 않는 경우
    #  두번째 경우는 현재 포도주양, 처음부터 전전전 포도주까지 먹은 양중에 가장 많이 먹을 수 방법으로 먹은 포도주(dp[전전])를 먹는 경우,즉 전 포도주를 안먹는 경우
    #  세번째 경우는 처음부터 전 포도주까지 먹은 양중에 가장 많이 먹을 수 방법으로 먹은 포도주(dp[전])를 먹는 경우, 즉 현재 포도주를 안먹는 경우

print(dp[n])