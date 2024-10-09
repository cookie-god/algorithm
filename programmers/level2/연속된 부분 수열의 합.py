def solution(sequence, k):
    answers = []
    sum = 0
    l = 0  # 맨 앞 위치 저장
    r = -1  # 맨 뒤 위치 저장

    while True:
        if sum < k:  # k보다 작은 경우
            r += 1  # 맨 뒤 위치 증가
            if r >= len(sequence):  # 범위를 넘는 경우 break
                break
            sum += sequence[r]  # 부분 수열합 계산
        else:  # k보다 큰 경우
            sum -= sequence[l]  # 맨 앞의 부분 수열 값 제거
            if l >= len(sequence):  # 범위를 넘는 경우 break
                break
            l += 1  # 맨 앞 위치 증가
        if sum == k:  # k와 같다면
            answers.append([l, r])  # 배열 삽입

    answers.sort(key=lambda x: (x[1] - x[0], x[0]))  # 둘의 차이가 작은대로, 같다면 앞의 원소를 기준으로
    return answers[0]
## DP 방식
#     answer = []
#     check = []
#     length = len(sequence)
#     dp = [[0] * length for _ in range(length)]

#     for i in range(length):
#         for j in range(length):
#             if i == j:
#                 dp[i][j] = sequence[j]

#     for i in range(1, length):
#         for j in range(i - 1, -1, -1):
#             dp[j][i] = dp[j][i-1] + dp[j+1][i] - dp[j+1][i-1]

#     for i in range(length):
#         for j in range(i, length):
#             if dp[i][j] == k:
#                 check.append([i, j, abs(i - j)])
#     check.sort(key=lambda x:x[2])

#     answer.append(check[0][0])
#     answer.append(check[0][1])

#     return answer