def solution(storey):
    answer = 0

    while storey:
        num = storey % 10

        if num > 5:  # 5보다 큰 경우
            storey += 10 - num
            answer += 10 - num
        elif num == 5 and (storey // 10) % 10 >= 5:  # 5이면서 앞의 자리 숫자가 5와 크거나 같은 경우 -> 95의 경우 1을 5번 더한 뒤 100을 1번 빼면 됨
            storey += 10 - num
            answer += 10 - num
        else:  # 5 이하인 경우
            answer += num

        storey //= 10

    return answer

solution(16)
solution(2554)
solution(95)