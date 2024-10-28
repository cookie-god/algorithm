from collections import Counter


def solution(topping):
    answer = 0
    counter = Counter(topping)  # 철수가 가진 롤케이크 개수 체크
    arr = set()  # 동생의 롤케이크 종류

    for t in topping:
        counter[t] -= 1  # 철수가 가진 롤케이크 종류 찾아 감소
        arr.add(t)  # 동생의 롤케이크 종류 증가

        if counter[t] == 0:  # 철수가 가진 롤케이크 종류가 아예 없다면 제거
            counter.pop(t)

        if len(counter) == len(arr):  # 두개의 크기가 같다면 정답
            answer += 1

    return answer