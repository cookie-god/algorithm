def solution(N, stages):
    answer = []
    stagesLen = len(stages)  # 스테이지 전체 길이
    stages.sort()  # 스테이지 정렬
    processed = []  # 처리한 스테이지를 담는 배열
    array = []  # 스테이지와 실패율을 담는 튜플 배열

    for i in range(1, N + 1):
        if i in stages:  # stages 배열에 포함된다면
            if i not in processed:  # 처리되지 않은 스테이지라면
                processed.append(i)  # 스테이지 처리배열 삽입
                array.append((i, stages.count(i) / stagesLen))  # 실패한 스테이지와 실패율 삽입
                stagesLen -= stages.count(i)  # 남은 스테이지의 개수 최신화
            else:  # 이미 처리된 스테이지이기 때문에 continue
                continue
        else:  # stages 배열에 포함되지 않는다면, 즉 실패한 유저가 없는 스테이지라면
            if i not in processed:  # 처리되지 않은 스테이지라면
                processed.append(i)  # 스테이지 처리배열 삽입
                array.append((i, 0))  # 아이템과 실패율 0을 삽입
            else:  # 이미 처리된 실패한 유저가 없는 스테이지라면 continue
                continue

    array.sort(key=lambda x: (-x[1], x[0]))  # 실패율 내림차순, 스테이지 오름차순 정렬

    for item in array:  # answer에 스테이지명 삽입
        answer.append(item[0])

    return answer

print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))
print(solution(4, [4, 4, 4, 4, 4]))