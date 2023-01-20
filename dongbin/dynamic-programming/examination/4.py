import sys

N = int(sys.stdin.readline().strip())
array = list(map(int, sys.stdin.readline().split()))
array.reverse()  # 가장 긴 증가하는 부분 수열을 구하는 것처럼 하기위해 reverse() 그러면 오름차순으로 구하면 됨
dp = [1 for _ in range(N)]  # dp[i]는 array[i]를 마지막으로 담는 가장 큰 부분 수열의 개수

for i in range(1, N):
    for j in range(0, i):
        if array[j] < array[i]:
            dp[i] = max(dp[i], dp[j] + 1)

print(N - dp[N - 1])

# 길이가 가장 긴 부분 수열 구하는 방법
# import sys
#
# N = int(sys.stdin.readline().strip())
# array = list(map(int, sys.stdin.readline().split()))
# array.reverse()
# dp = [1 for _ in range(N)]
#
# for i in range(1, N):
#     for j in range(0, i):
#         if array[j] < array[i]:
#             dp[i] = max(dp[i], dp[j] + 1)
# print(dp)