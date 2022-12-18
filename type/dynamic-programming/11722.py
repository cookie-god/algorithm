import sys

N = int(sys.stdin.readline().strip())
array = list(map(int, sys.stdin.readline().split()))
array.insert(0, 0)  # array 맨 앞에 0 삽입
dp = [1 for _ in range(N + 1)]  # dp배열 각 1로 초기화, dp[i]는 i번째 인덱스에서 가장 많은 부분 감소 수열 개수

for i in range(2, N + 1):  # for문 돌때마다 dp[i] 확정됨
    for j in range(i):
        if array[i] < array[j]:  # 만약 array[j]가 더 크다면 부분 감소 수열
            dp[i] = max(dp[i], dp[j] + 1)  # 현재 dp[i] 결정하는 곳. 이전까지의 dp배열에 1을 더한 것과 현재 dp배열 비교

# print(dp)
print(max(dp))