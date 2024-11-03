from itertools import combinations
from collections import defaultdict


def solution(orders, course):
    answer = []

    for c in course:
        combiCount = defaultdict(int)  # 각 조합별 개수를 저장하는 딕셔너리
        maxOrder = []  # 가장 큰 value를 갖는 key값 저장하는 리스트
        for order in orders:
            orderCombi = combinations(list(order), c)  # 코스의 단품 개수만큼 조합 추출
            for oc in orderCombi:
                orderString = ''.join(sorted(oc))  # 문자열 정렬해서 합침
                combiCount[orderString] += 1  # 딕셔너리에 해당 키값의 value 증가
        maxOrder = [k for k, v in combiCount.items() if
                    ((v == max(combiCount.values())) and v >= 2)]  # v가 maxValue와 같고, 2이상인 경우
        answer.extend(maxOrder)  # 리스트 다 제거해서 삽입
    answer = sorted(answer)  # 알파벳 순서로 정렬

    # 시간 초과
    #     result = []
    #     menu = []
    #     menu = set(menu)
    #     for o in orders:
    #         for i in range(len(o)):
    #             menu.add(o[i])

    #     menu = list(menu)
    #     menu.sort()
    #     dict = defaultdict(list)
    #     maxValueDict = defaultdict(int)

    #     for c in course:
    #         for combi in list(combinations(menu, c)):
    #             sum = 0
    #             for order in orders:
    #                 flag = True
    #                 for com in combi:
    #                     if com not in order: # 하나라도 포함 되지 않는 다면
    #                         flag = False
    #                         break
    #                 if flag:
    #                     sum += 1
    #             if sum > 1:
    #                 if maxValueDict[c] < sum:
    #                     maxValueDict[c] = sum
    #                     dict[c].clear()
    #                     dict[c].append(combi)
    #                 elif maxValueDict[c] == sum:
    #                     maxValueDict[c] = sum
    #                     dict[c].append(combi)

    #     for key, value in dict.items():
    #         for v in value:
    #             answer.append(''.join(v))

    #     answer.sort()

    return answer