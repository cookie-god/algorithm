def possible(answer):  # 가능한지 체크하는 함수
    for x, y, structure in answer:
        if structure == 0:  # 기둥인 경우
            # 바닥 바로 위, 보의 오른쪽 끝부분에 연결된 경우, 보의 왼쪽 끝부분에 연결된 경우, 다른 기둥의 위인 경우
            if y == 0 or [x - 1, y, 1] in answer or [x, y, 1] in answer or [x, y - 1, 0] in answer:
                continue
            return False
        elif structure == 1:  # 보인 경우
            # 보의 왼쪽 끝이 기둥과 연결되어 있는 경우, 보의 오른쪽 끝이 기둥과 연결되어 있는 경우, 다른 보와 동시에 연결이 되어 있는 경우
            if [x, y - 1, 0] in answer or [x + 1, y - 1, 0] in answer or (
                    [x - 1, y, 1] in answer and [x + 1, y, 1] in answer):
                continue
            return False
    return True


def solution(n, build_frame):
    answer = []
    for item in build_frame:
        x, y = item[0], item[1]

        if item[3] == 1:  # 설치하는 경우
            answer.append([x, y, item[2]])  # 우선 삽입
            if not possible(answer):  # 불가능한 경우
                answer.remove([x, y, item[2]])  # 다시 제거

        elif item[3] == 0:  # 제거하는 경우
            answer.remove([x, y, item[2]])  # 우선 제거
            if not possible(answer):  # 불가능한 경우
                answer.append([x, y, item[2]])  # 다시 삽입

    answer.sort()  # 정렬
    return answer

print(solution(5, [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]))
print(solution(5, [[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]))

# def possible(answer):
#     for x, y, structure in answer:
#         if structure == 0:
#             if y == 0 or [x - 1, y, 1] in answer or [x, y, 1] in answer or [x, y - 1, 0] in answer:
#                 continue
#             return False
#         elif structure == 1:
#             if [x, y - 1, 0] in answer or [x + 1, y - 1, 0] in answer or (
#                     [x - 1, y, 1] in answer and [x + 1, y, 1] in answer):
#                 continue
#             return False
#     return True
#
#
# def solution(n, build_frame):
#     answer = []
#     for item in build_frame:
#         x, y = item[0], item[1]
#         flag = True
#
#         if item[3] == 1:
#             if item[2] == 0:
#                 if y == 0:
#                     answer.append([item[0], item[1], item[2]])
#                 else:
#                     for check in answer:
#                         if check[2] == 0:
#                             if x == check[0] and y == check[1] + 1:
#                                 answer.append([item[0], item[1], item[2]])
#                                 break
#                         elif check[2] == 1:
#                             if x == check[0] + 1 and y == check[1]:
#                                 answer.append([item[0], item[1], item[2]])
#                                 break
#                             elif x - 1 == check[0] and y + 1 == check[1]:
#                                 answer.append([item[0], item[1], item[2]])
#                                 break
#
#             elif item[2] == 1:
#                 for check in answer:
#                     if check[2] == 0:
#                         if x == check[0] and y == check[1] + 1:
#                             answer.append([item[0], item[1], item[2]])
#                             break
#                         elif x + 1 == check[0] and y - 1 == check[1]:
#                             answer.append([item[0], item[1], item[2]])
#                             break
#                     elif check[2] == 1:
#                         if x == check[0] + 1 and y == check[1]:
#                             answer.append([item[0], item[1], item[2]])
#                             break
#
#         elif item[3] == 0:
#             answer.remove([x, y, item[2]])
#             if not possible(answer):
#                 answer.append([x, y, item[2]])
#
#     answer.sort()
#     return answer