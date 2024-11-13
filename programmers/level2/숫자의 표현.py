def solution(n):
    answer = 1  # 자기 자신 포함

    for i in range(1, n // 2 + 1):  # 절반까지만 비교
        sum = 0
        while sum < n:
            sum += i
            i += 1
            if sum == n:  # n과 비교
                answer += 1
                break

    return answer