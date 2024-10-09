from collections import deque


def makeTime(hourMinute):
    hour, minute = hourMinute.split(":")
    hour = int(hour) * 60
    minute = int(minute)
    return hour + minute


def solution(plans):
    answer = []
    num = len(plans)
    for plan in plans:
        plan[1] = makeTime(plan[1])
        plan[2] = int(plan[2])

    notAction = deque()
    plans.sort(key=lambda x: x[1])  # 과제 시작 시간 순서대로 정렬

    for i in range(num):
        if i == num - 1:  # 마지막 과제인 경우 스택에 삽입
            notAction.append((plans[i][0], plans[i][1], plans[i][2]))
            break

        if plans[i][1] + plans[i][2] <= plans[i + 1][1]:  # 과제를 시작할 수 있는 경우
            answer.append(plans[i][0])  # 과제 완료
            tempTime = plans[i + 1][1] - (plans[i][1] + plans[i][2])  # 다음 과제까지 남은 시간 계산

            while tempTime != 0 and notAction:  # 다음 과제까지 시간이 남고 미진행 과제가 있는 경우
                subject, start, playTime = notAction.pop()  # 미진행 과제 추출
                if tempTime >= playTime:  # 미진행 과제 진행 가능한 경우
                    answer.append(subject)  # 과제 완료
                    tempTime -= playTime  # 다음 과제까지 남은 시간 갱신
                else:  # 미진행 과제 불가능 한 경우
                    notAction.append((subject, start, playTime - tempTime))  # 미진행 스택에 다시 삽입
                    tempTime = 0  # 남은시간 0으로 초기화
        else:  # 과제를 시작할 수 없는 경우
            notAction.append(
                (plans[i][0], plans[i][1], plans[i][2] - (plans[i + 1][1] - plans[i][1])))  # 미진행 과제에 남은 과제 시간 갱신해서 삽입

    while notAction:  # 미진행 과제 삽입
        answer.append(notAction.pop()[0])

    return answer