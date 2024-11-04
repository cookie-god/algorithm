from collections import deque, defaultdict


def solution(n, k, cmd):
    answer = ''
    linkedList = {i: [i - 1, i + 1] for i in range(n)}  # 더블링크드리스트 처럼 사용
    table = ["O"] * n  # 초기화
    delete = deque()  # 스택

    for c in cmd:
        c = c.split()  # 띄어쓰기 분할

        if c[0] == "D":
            for _ in range(int(c[1])):
                k = linkedList[k][1]  # 현재 위치 증가

        elif c[0] == "U":
            for _ in range(int(c[1])):
                k = linkedList[k][0]  # 현재 위치 감소
        elif c[0] == "C":
            prev, next = linkedList[k]
            table[k] = "X"
            delete.append((prev, k, next))  # 삭제큐에 삽입

            if next == n:  # 삭제된 행이 가장 마지막 행인 경우 바로 이전 행을 선택
                k = linkedList[k][0]
            else:  # 다음 행을 현재 위치로 선택
                k = linkedList[k][1]

            if prev == -1:
                linkedList[next][0] = prev  # 다음행의 이전이 처음인 것을 저장, 이전이 없음
            elif next == n:
                linkedList[prev][1] = next  # 이전행의 다음이 마지막인 것을 저장, 다음이 없음
            else:
                linkedList[prev][1] = next
                linkedList[next][0] = prev
        else:
            prev, now, next = delete.pop()
            table[now] = "O"

            if prev == -1:
                linkedList[next][0] = now  # 다음행의 이전이 현재인 것을 저장, 이전이 없음
            elif next == n:
                linkedList[prev][1] = now  # 이전행의 다음이 현재인 것을 저장, 다음이 없음
            else:
                linkedList[prev][1] = now
                linkedList[next][0] = now
    return "".join([x for x in table])

#     arr = [i for i in range(n)] # 존재 여부 체크
#     stack = deque()

#     now = k # 현재 위치
#     cnt = n # 남아 있는 인원 수

#     for c in cmd:
#         if c == "C": # 삭제
#             # 스택에 넣기
#             stack.append((now, arr[now])) # 현재 위치, 값
#             # 이 전 원소들 모두 하나씩 땡기기
#             arr[now:cnt] = arr[now+1:cnt]
#             # 현재 남아 있는 인원 수 위치에 -1 삽입
#             arr.append(-1)
#             # 현재 인원수 감소
#             cnt -= 1
#             # 삭제된 행이 가장 마지막 행인 경우
#             if now == cnt:
#                 now -= 1

#         elif c == "Z": # 되돌리기
#             # 스택에서 값 꺼내기
#             idx, value = stack.pop()
#             # 이미 비어있는 가장 마지막 원소라면
#             if arr[idx] == -1:
#                 arr[idx] = value
#             else: # 중간에 껴있는 원소라면
#                 arr[idx+1:cnt] = arr[idx:cnt] # 원소 복사
#                 del arr[-1] # 가장 마지막 추가된 원소 제거
#                 arr[idx] = value # 비어있는 위치에 값 삽입
#                 # 복구한 위치가 now보다 작은 경우
#                 if now > idx:
#                     now += 1 # 현재 가리키는 곳 위치 변경
#         else:
#             location, value = c.split(" ") # D, U인 경우 위치와 값 확인
#             if location == "D":
#                 now += int(value)
#             else:
#                 now -= int(value)

#     for i in range(n):
#         if i in arr:
#             answer += "O"
#         else:
#             answer += "X"

# return answer