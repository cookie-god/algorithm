import sys

N = int(sys.stdin.readline().strip())
array = list(map(int, sys.stdin.readline().split()))
array.insert(0, 0)  # array 맨 첫번째 원소에 0 삽입
dp = [0 for _ in range(N + 1)]
dp[1] = array[1]  # dp[1]은 array[1]과 같음

for i in range(2, N + 1):
    for j in range(1, i):  # i 인덱스 안에서 비교하는 이유는 j부터 i까지 비교하면서 dp[i]를 확실히 정하기 위해서
        if array[i] > array[j]:  # array[i]가 array[j]보다 큰 경우 부분 수열이기 때문에 dp[i]를 최신화 한다
            dp[i] = max(dp[i], dp[j] + array[i])  # dp[j]는 이미 j 인덱스까지 이미 확정된 오름차순의 숫자의 수이므로 여기에 array[i]를 더한 것과 기존의 dp[i]와 비교한다.
        else:
            dp[i] = max(dp[i], array[i])  # dp[i]보다 array[i]와 비교해서 만약 더 크다면 array[i]로 변경

print(max(dp))