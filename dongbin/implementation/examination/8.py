from itertools import permutations


def solution(n, weak, dist):
    distLength = len(dist)
    weakLength = len(weak)
    for i in range(weakLength):
        weak.append(weak[i] + n)

    permu = list(permutations(dist, distLength))  # 순서를 고려한 모든 경우의 수
    answer = distLength + 1  # 친구의 최대 수를 넘을 수 없게 설정
    for start in range(weakLength):  # 맨 처음 위치부터 탐색 시작
        for friend in permu:  # permutations로 나온 모든 친구 투입 순서
            count = 1  # 투입한 친구 수
            position = weak[start] + friend[count - 1]  # 첫 친구가 커버할 수 있는 범위 설정
            for i in range(start, start + weakLength):  # 시작 위치부터 끝 지점까지 탐색
                if position < weak[i]:  # 친구가 커버할 수 있는 범위보다 약한 지점이 더 큰 경우
                    count += 1  # 새로운 친구 투입
                    if count > distLength:  # 모든 친구가 이미 투입된 경우에는 탈출
                        break
                    position = weak[i] + friend[count - 1]  # 다음 친구가 커버할 수 있는 범위 설정
            answer = min(answer, count)  # 최소값 체크

    if answer > distLength:  # 친구들로 점검하지 못한다면 -1 리턴
        return -1
    return answer


print(solution(12, [1, 5, 6, 10], [1, 2, 3, 4]))
print(solution(12, [1, 3, 4, 9, 10], [3, 5, 7]))