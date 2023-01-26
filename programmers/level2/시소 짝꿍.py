from itertools import combinations
from collections import Counter

def solution(weights):
    answer = 0
    count = Counter(weights)
    for k, v in count.items():
        if v > 1:
            answer += v * (v - 1) // 2

    weights = list(set(weights))
    for item in weights:
        for check in (3 / 4, 2 / 3, 2 / 4):
            if item * check in weights:
                answer += count[item] * count[item * check]

    #     case = list(combinations(weights, 2))
    #     case.sort(key=lambda x: (x[0]))

    #     for item in case:
    #         minNum = min(item[0], item[1])
    #         maxNum = max(item[0], item[1])
    #         temp = maxNum / minNum

    #         if temp in [1, 3/2, 4/3, 4/2]:
    #             answer += 1

    return answer

print(solution([100,180,360,100,270]))