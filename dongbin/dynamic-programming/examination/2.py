import sys
n = int(sys.stdin.readline().strip())
array = []
dp = [[0] * i for i in range(1, n + 1)]  # dp[i][j]는 i, j까지 오는데 얻을 수 있는 가장 큰 정수값
for i in range(n):
    if i == 0:
        array.append(list(sys.stdin.readline().strip()))
    else:
        array.append(list(map(int, sys.stdin.readline().split())))

array[0][0] = int(array[0][0])  # str을 int로 변환
dp[0][0] = array[0][0]  # dp[0][0] 최신화
dp[1][0] = array[0][0] + array[1][0]  # dp[1][0] 최신화
dp[1][1] = array[0][0] + array[1][1]  # dp[1][1] 최신화

for i in range(2, n):  # 2행부터 검사
    lenItem = len(array[i])  # 각 행의 길이 저장
    for j in range(lenItem):  # 각 행의 길이 만큼 조사
        if j == 0:  # 첫번째 열인 경우
            dp[i][j] = array[i][j] + dp[i - 1][j]  # 자신의 오른쪽 위에 있는 것만 가져올 수 있음
        elif j == lenItem - 1:  # 마지막 열인 경우
            dp[i][j] = array[i][j] + dp[i-1][j - 1]  # 자신의 왼쪽 위에 있는 것만 가져올 수 있음
        else:  # 그 외의 경우
            dp[i][j] = array[i][j] + max(dp[i - 1][j - 1], dp[i - 1][j])  # 자신의 왼쪽 위와 오른쪽 위 비교해서 큰 값 가져옴

result = 0
for i in range(n):
    for item in dp[i]:
        if item >= result:
            result = item
print(result)