def solution(numbers, hand):
    answer = ''
    leftFinger = (3, 0)  # * 위치
    rightFinger = (3, 2)  # # 위치

    for number in numbers:
        if number in [1, 4, 7]:
            leftFinger = (number // 3, 0)  # 왼쪽 손가락 이동
            answer += "L"
        elif number in [3, 6, 9]:
            rightFinger = (number // 3 - 1, 2)  # 오른쪽 손가락 이동
            answer += "R"
        else:  # 가운데 숫자인 경우
            nowIndex = ()  # 현재 위치
            if number == 0:  # 0인 경우는 따로 지정
                nowIndex = (3, 1)
            else:
                nowIndex = (number // 3, 1)  # 2, 5, 8에 대한 위치 지정
            leftDistance = abs(nowIndex[0] - leftFinger[0]) + abs(nowIndex[1] - leftFinger[1])  # 왼손으로 부터의 거리
            rightDistance = abs(nowIndex[0] - rightFinger[0]) + abs(nowIndex[1] - rightFinger[1])  # 오른손으로 부터의 거리

            if leftDistance > rightDistance:  # 오른손의 거리가 더 짧다면, 오른손으로 이동
                rightFinger = nowIndex
                answer += "R"
            elif rightDistance > leftDistance:  # 왼손의 거리가 더 짧다면, 왼손으로 이동
                leftFinger = nowIndex
                answer += "L"
            else:  # 같아면 hand에 따라 변경
                if hand == "right":
                    rightFinger = nowIndex
                    answer += "R"
                else:
                    leftFinger = nowIndex
                    answer += "L"

    return answer