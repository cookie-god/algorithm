from collections import deque


def solution(numbers, target):
    answer = 0
    length = len(numbers)
    resultQueue = deque()  # 숫자를 더한거 또는 뺀거의 결과물 저장하는 큐
    operationQueue = deque()  # resultQueue에서 popleft한 숫자에서 다음 숫자를 더하거나 뺀 값을 저장하는 큐
    resultQueue.append((numbers[0], numbers[0]))  # 맨 첫번째 플러스 값 resultQueue에 삽입
    resultQueue.append((numbers[0], -numbers[0]))  # 맨 첫번째 마이너스 값 resultQueue에 삽입

    for i in range(1, length):  # 두번째 원소부터
        while resultQueue:  # 결과물 큐 확인
            now, sum = resultQueue.popleft()
            operationQueue.append((numbers[i], sum + numbers[i]))  # 더한값 operationQueue에 삽입
            operationQueue.append((numbers[i], sum - numbers[i]))  # 뺀값 operationQueue에 삽입
        resultQueue = operationQueue.copy()  # 결과물 저장하는 큐에 삽입
        operationQueue.clear()  # operationQueue 초기화

    while resultQueue:  # 결과물 체크
        now, sum = resultQueue.popleft()
        if sum == target:
            answer += 1

    return answer