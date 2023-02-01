from collections import Counter

def solution(k, tangerine):
    answer = 0
    count = Counter(tangerine)
    array = []
    for n, v in count.items():
        array.append((n, v))

    array.sort(key=lambda x: -x[1])

    for item in array:
        k -= item[1]
        answer += 1
        if k <= 0:
            break

    return answer

print(solution(6, [1, 3, 2, 5, 4, 5, 2, 3]))
print(solution(4, [1, 3, 2, 5, 4, 5, 2, 3]))
print(solution(2, [1, 1, 1, 1, 2, 2, 2, 3]))