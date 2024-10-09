def solution(diffs, times, limit):
    answer = 0
    start = 1  # 레벨 1부터
    end = 10 ** 15  # limit의 크기까지

    def caculate(level):
        sum = 0  # 소요시간 계산
        for i in range(len(diffs)):
            if diffs[i] <= level:  # 퍼즐 틀리지 않는 경우
                sum += times[i]  # 퍼즐 해결한 경우
            else:
                tc = times[i]  # 현재 시간
                tp = 0  # 이전 시간
                if i - 1 >= 0:  # 첫번째 원소가 아닌 경우
                    tp = times[i - 1]  # 이전 시간 셋팅
                sum += (tc + tp) * (diffs[i] - level) + tc  # 소요시간 셋팅
        return sum

    while True:
        if start >= end:  # 탐색 종료 조건
            break

        mid = (end + start) // 2  # 중간값 계산
        sum = caculate(mid)  # 중간값을 레벨로 체크

        if sum > limit:  # 합계가 더 크다면 렙이 더 올라가야함
            start = mid + 1
        else:  # 합계가 더 작다면 렙을 낮춰야함
            end = mid

    answer = start  # 가장 최솟값이 렙
    return answer