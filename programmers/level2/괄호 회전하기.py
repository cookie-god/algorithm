from collections import deque


def solution(s):
    answer = 0
    length = len(s)  # 문자열의 길이
    queue = deque(s)  # 큐 삽입
    count = 0  # 실행 횟수

    while count < length:  # 문자열의 길이만큼 실행
        count += 1  # 실행횟수 증가
        stack = deque()  # 스택 생성
        flag = False  # 스택에 데이터가 삽입이 되었는지 체크하는 flag값
        for i in range(length):  # 큐 내부 데이터 체크
            if queue[i] != "}" and queue[i] != "]" and queue[i] != ")":  # 여는 괄호라면 스택에 삽입
                stack.append(queue[i])
                flag = True  # 스택에 데이터 삽입 여부 값 변경
            else:  # 닫는 괄호라면
                if len(stack) != 0:  # 스택이 비어있지 않다면
                    if queue[i] == "}" and stack[-1] == "{":  # 괄호 매칭시켜 stack 원소 제거
                        stack.pop()
                    if queue[i] == "]" and stack[-1] == "[":  # 괄호 매칭시켜 stack 원소 제거
                        stack.pop()
                    if queue[i] == ")" and stack[-1] == "(":  # 괄호 매칭시켜 stack 원소 제거
                        stack.pop()
        if len(stack) == 0 and flag:  # 스택이 비었고, 스택에 데이터를 삽입한 이력이 있는 경우 정답
            answer += 1
        queue.append(queue.popleft())  # 앞의 원소를 맨 뒤로 삽입

    return answer