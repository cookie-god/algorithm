# 시간 초과
def solution1(numbers):
    answer = []
    count = 0
    lenNumbers = len(numbers)
    for item in numbers:
        count += 1
        if item == max(numbers):
            answer.append(-1)
            continue

        if count == lenNumbers:
            answer.append(-1)
        else:
            flag = False
            for i in range(count, lenNumbers):
                if item < numbers[i]:
                    answer.append(numbers[i])
                    flag = True
                    break

            if flag == False:
                answer.append(-1)

    return answer


# 스택으로 해결
def solution2(numbers):
    stack = []
    answer = [0] * len(numbers)

    for i in range(len(numbers)):
        while stack and numbers[stack[-1]] < numbers[i]:  # 스택이 있는 경우 그리고 그 스택의 가장 위 값이 비교하는 숫자보다 작은 경우
            answer[stack.pop()] = numbers[i]  # 정답 인덱스에 작은 숫자 삽입
        stack.append(i)  # 스택에 인덱스 삽입
    while stack:  # 마지막 원소에 대해서 -1 처리
        answer[stack.pop()] = -1

    return answer

print(solution1([2, 3, 3, 5]))
print(solution1([9, 1, 5, 3, 6, 2]))

print(solution2([2, 3, 3, 5]))
print(solution2([9, 1, 5, 3, 6, 2]))