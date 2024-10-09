def solution(n, m, section):
    answer = 0
    visited = [1 for _ in range(n + 1)]
    for s in section:  # 페인트 칠하지 않은 영역을 0으로 표시
        visited[s] = 0
    sectionLength = len(section)
    section.sort(reverse=True)  # 큰수에서 작은수를 빼게 하기 위해 역순 정렬

    for i in range(sectionLength):
        if i != sectionLength - 1:  # 마지막 수가 아니라면
            if visited[section[i]] == 0:  # 이미 칠하지 않은 경우만 조사하도록
                for j in range(m):  # m의 길이만큼 조사
                    visited[section[i] - j] = 1  # 칠하지 않은 영역부터 m번 visited 배열 1로 변경
                answer += 1

    if visited[section[-1]] == 0:  # 마지막 방문 기록이 없는 경우 칠하기
        answer += 1
        visited[section[-1]] == 1

    return answer