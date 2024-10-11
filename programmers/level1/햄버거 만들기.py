from collections import deque


def solution(ingredient):
    answer = 0
    length = len(ingredient)
    stack = deque()  # 스택처럼 deque 사용

    for i in range(length):
        stack.append(ingredient[i])  # 스택에 삽입
        if len(stack) >= 4 and ingredient[i] == 1:  # 4개 이상 쌓여있고, 빵인 경우
            if stack[-2] == 3 and stack[-3] == 2 and stack[-4] == 1:  # 스택에 쌓여있는 원소 조회시 고기, 야채, 빵 순서로 쌓여 있는 경우에만
                stack.pop()
                stack.pop()
                stack.pop()
                stack.pop()
                # 4개의 재료 빼기
                answer += 1

    return answer