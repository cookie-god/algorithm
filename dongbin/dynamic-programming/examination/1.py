import sys

def dynamicProgramming():
    maxNum = 0
    dp = [[0] * m for _ in range(n)]  # dp[i][j]는 i, j까지 이동했을 때 얻을 수 있는 가장 많은 금광값
    dp[0][0] = array[0][0]
    dp[1][0] = array[1][0]
    dp[2][0] = array[2][0]

    for i in range(1, m):  # 첫번째 열부터 비교
        for j in range(n):  # 첫번째 행부터 비교
            if j == 0:  # 가장 첫번째 행에 있다면 오른쪽과 오른쪽 아래 비교
                dp[j][i] = max(dp[j][i - 1] + array[j][i], dp[j + 1][i - 1] + array[j][i])
            elif j == n - 1:  # 가장 마지막 행에 있다면 오른쪽과 오른쪽 위 비교
                dp[j][i] = max(dp[j - 1][i - 1] + array[j][i], dp[j][i - 1] + array[j][i])
            else:  # 중간행에 있다면 오른쪽, 오른쪽 아래, 오른쪽 위 비교
                dp[j][i] = max(dp[j - 1][i - 1] + array[j][i], dp[j][i - 1] + array[j][i], dp[j + 1][i - 1] + array[j][i])

    # 가장 큰 값 추출
    for item in dp:
        for num in item:
            if num >= maxNum:
                maxNum = num
    return maxNum


T = int(sys.stdin.readline().strip())
for _ in range(T):
    n, m = map(int, sys.stdin.readline().split())
    data = list(map(int, sys.stdin.readline().split()))
    idx = 0
    array = [[0] * m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            array[i][j] = data[idx]
            idx += 1
    result = dynamicProgramming()
    print(result)
