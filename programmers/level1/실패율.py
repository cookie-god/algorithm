def solution(N, stages):
    answer = []
    stagesLen = len(stages)
    stages.sort()
    processed = []
    array = []

    for i in range(1, N + 1):
        if i in stages:
            if i not in processed:
                processed.append(i)
                array.append((i, stages.count(i) / stagesLen))
                stagesLen -= stages.count(i)
            else:
                continue
        else:
            if i not in processed:
                processed.append(i)
                array.append((i, 0))
            else:
                continue

    array.sort(key=lambda x: (-x[1], x[0]))

    for item in array:
        answer.append(item[0])

    return answer