def solution(n, times):
    answer = 0
    start = 0  # 총 걸릴 수 있는 시간의 최소값
    end = max(times) * n  # 총 걸릴 수 있는 시간의 최대값

    while start <= end:
        mid = (start + end) // 2
        people = 0  # mid 분에서 총 조사한 사람의 수

        for time in times:  # 심사대 별로 체크
            people += mid // time  # 심사대별로 총 가능한 인원수 더함

            if people >= n:  # 이미 n명 이상 가능한 시간이라면 탈출
                break

        if people >= n:  # n명보다 같거나 더 많은 인원수를 mid분 안에 심사할 수 있다면
            answer = mid  # 후보 셋팅
            end = mid - 1  # 최소값을 구하기 위해 탐색 기준값 낮춤
        else:  # n명보다 낮기 때문에 탐색 기준값을 올려야함
            start = mid + 1

    return answer