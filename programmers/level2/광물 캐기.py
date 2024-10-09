def solution(picks, minerals):
    answer = 0
    sum = 0  # 곡괭이 개수 체크
    for i in picks:
        sum += i

    num = sum * 5  # 곡괭이 사용 카운트 체크
    if len(minerals) > sum:  # 광물의 개수보다 사용 개수가 더 많은 경우
        minerals = minerals[:num]  # 캘 수 있는 광물 다시 셋팅

    new_minerals = [[0, 0, 0] for _ in range((len(minerals) // 5 + 1))]  # 5번씩 시도하기 때문에 5번 안에 어떤 광물들이 있는지 조사
    for i in range(len(minerals)):
        if minerals[i] == 'diamond':
            new_minerals[i // 5][0] += 1
        elif minerals[i] == 'iron':
            new_minerals[i // 5][1] += 1
        elif minerals[i] == 'stone':
            new_minerals[i // 5][2] += 1

    # 5개씩 나눈광물의 순서를 다이아몬드, 철, 돌 순서대로 정렬해준다.
    new_minerals.sort(key=lambda x: (-x[0], -x[1], -x[2]))

    for mineral in new_minerals:
        d, i, s = mineral
        print(d, i, s)
        for p in range(len(picks)):
            if p == 0 and picks[p] > 0:  # dia 곡괭이가 남았다면
                picks[p] -= 1
                answer += d + i + s
                break
            elif p == 1 and picks[p] > 0:  # iron 곡괭이
                picks[p] -= 1
                answer += 5 * d + i + s
                break
            elif p == 2 and picks[p] > 0:  # stone 곡괭이
                picks[p] -= 1
                answer += 25 * d + 5 * i + s
                break

    return answer