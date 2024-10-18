from collections import deque


def solution(tickets):
    queue = deque()
    n = len(tickets)
    for i in range(n):
        if tickets[i][0] == "ICN":  # 첫 시작은 인천
            visit = [0 for i in range(n)]  # 티켓 사용 이력 체크
            visit[i] = -1  # 해당 티켓 사용
            queue.append([tickets[i][1], tickets[i], visit])  # 큐에 도착지, 비행기로 이동한 경로, 티켓 사용 이력 삽입
    allFlight = []  # 전체 순항을 다 한 경우
    while queue:
        current, flightInfo, visit = queue.popleft()
        if len(flightInfo) == n + 1:  # 전체 순항을 다 한 경우
            allFlight.append(flightInfo)
            continue
        for i in range(n):
            if tickets[i][0] == current:  # 다른 티켓이 현재 도착지인 경우
                if visit[i] == 0:  # 방문한 이력이 없는 경우
                    newVisit = visit[:]  # 기존 티켓 사용 이력을 복사
                    newFlightInfo = flightInfo[:]  # 비행기로 이동한 경로 복사
                    newVisit[i] = -1  # 티켓 사용 여부 변경
                    newFlightInfo.append(tickets[i][1])  # 비행기로 이동한 경로에 추가
                    queue.append([tickets[i][1], newFlightInfo, newVisit])

    allFlight.sort()
    return allFlight[0]