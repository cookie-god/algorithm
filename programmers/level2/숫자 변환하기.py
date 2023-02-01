def solution(x, y, n):
    answer = 0
    dp = [1e7] * (y + 1)  # y값만큼 dp 배열 생성
    dp[x] = 0  # x 연산 값은 0번이기 때문

    for i in range(x + 1, y + 1):
        if dp[i - n] != 1e7:  # 특정 수에서 n을 뺏는데, 그 값이 1e7이 아니라면 계산 가능
            dp[i] = min(dp[i], dp[i - n] + 1)  # 기존 dp[i]와 dp[i - n] + 1 비교해서 작은 수 대입

        if i % 2 == 0 and dp[i // 2] != 1e7:  # 특정 수가 2로 나누어 떨어지고, dp[i // 2]이 1e7이 아니라면 계산 가능
            dp[i] = min(dp[i], dp[i // 2] + 1)  # 기존 dp[i]와 dp[i // 2] + 1 비교해서 작은 수 대입

        if i % 3 == 0 and dp[i // 3] != 1e7:  # 특정 수가 3으로 나누어 떨어지고, dp[i // 3]이 1e7이 아니라면 계산 가능
            dp[i] = min(dp[i], dp[i // 3] + 1)  # 기존 dp[i]와 dp[i // 3] + 1 비교해서 작은 수 대입

    if dp[y] == 1e7:  # 1e7이라면 계산 불가능한 수이므로 -1 대입
        answer = -1
    else:
        answer = dp[y]

    return answer

print(solution(10, 40, 5))
print(solution(10, 40, 30))
print(solution(2, 5, 4))