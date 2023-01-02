import sys

N = int(sys.stdin.readline().strip())
arr = list(map(int, sys.stdin.readline().split()))
arr.insert(0, 0)
dp = [0 for _ in range(N + 1)]

idx = 1
dp[idx] = arr[idx]
sum = 0


for i in range(1, N + 1):
    sum += arr[i]
    if dp[idx] < sum:
        idx += 1
        dp[idx] = sum;
    if sum < 0:
        sum = 0

print(dp[idx])