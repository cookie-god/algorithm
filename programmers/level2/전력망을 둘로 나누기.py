from collections import deque, defaultdict


def bfs(array, start):
    visited = [start]  # 방문 기록 정리
    queue = deque()
    queue.append(start)  # 시작 지점 큐 삽입

    while queue:
        location = queue.popleft()  # 현재 위치 노출
        for newLocation in array[location]:
            if newLocation not in visited:  # 방문 기록에 있지 않는 경우
                visited.append(newLocation)  # 방문 기록
                queue.append(newLocation)  # 큐에 삽입

    return len(visited)  # 방문한 곳 위치 리턴


def solution(n, wires):
    answer = []

    for wire1 in wires:
        array = defaultdict(list)  # 끊고 항상 새로 만들기 위해 새로 생성
        for wire2 in wires:
            if wire1 == wire2:  # 둘이 같으면 연결 X
                continue
            array[wire2[0]].append(wire2[1])
            array[wire2[1]].append(wire2[0])

        # 끊은 정점으로 부터 각각 시작
        one = bfs(array, wire1[0])
        two = bfs(array, wire1[1])
        answer.append(abs(one - two))  # 절대값 제거한 것 추가

    return min(answer)  # 최소값 출력