import sys

# N, K = map(int, sys.stdin.readline().split())
# arr = list(map(int, sys.stdin.readline().split()))
# plugs = []  # 플러그에 꽂힌 전자기기들을 저장하는 리스트
# usages = []  # 인덱스와 남은 전자기기 계산이 저장되는 변수를 저장하는 튜플 리스트
# result = 0  # 플러그 변경한 횟수
# firstInsertCount = 0  # 플러그 꽂기 시도한 횟수가 저장되는 변수
# sum = 0  # 남은 전자기기 계산이 저장되는 변수
#
# # 플러그 삽입
# for i in range(K):
#     # 플러그가 꽉 찬다면 탈출
#     if len(plugs) == N:
#         break
#
#     # 전자기기가 플러그에 포함되지 않았다면 추가
#     if arr[i] not in plugs:
#         plugs.append(arr[i])
#
#     # 플러그 꽂기 시도한 횟수 추가
#     firstInsertCount += 1
#
# # 플러그 꽂기 시도한 횟수부터 끝까지
# for i in range(firstInsertCount, K):
#     # 플러그에 꽂힌 전자기기랑 다른 경우
#     if arr[i] not in plugs:
#         # 플러그에서 비교
#         usages = []  # usage 초기화
#         for j in range(N):
#             sum = 0  # 남은 전자기기 개수 초기화
#             # 남아있는 전자기기 비교
#             for k in range(i + 1, K):
#                 # 플러그에 꽂힌 전자기기와 남은 전자기기들의 개수 비교
#                 if plugs[j] == arr[k]:
#                     sum += 1
#             usages.append((j, sum))  # 플러그의 인덱스와 남아있는 전자기기의 개수 삽입
#         usages.sort(key=lambda x: x[1])
#         print(usages[0][0])
#         plugs[usages[0][0]] = arr[i]
#         result += 1
#
#
# print(result)

N, K = map(int, input().split())
scheduling = list(map(int, input().split()))

adaptor = [0] * N
count = 0
scheduling_idx = 0
tmp = 0
tmp_i = 0

for i in scheduling:
    # 멀티탭에 같은 전기용품이 있을 때
    if i in adaptor:
        pass
    # 멀티탭이 아직 채워지지 않았을 때
    elif 0 in adaptor:
        adaptor[adaptor.index(0)] = i
    # 멀티탭에 빈자리 없고 현재 꽂혀 있는 전기용품들과 다를 때
    else:
        for j in adaptor:
            # 현재 꽂혀있는 전기용품이 더 이상 사용되지 않는다면
            if j not in scheduling[scheduling_idx:]:
                tmp = j
                break
            #현재 꽂혀있는 전기용품이 이후에도 사용될 때
            elif scheduling[scheduling_idx:].index(j) > tmp_i:  # 꽂혀있는 것들 중 여러 개가 다시 사용될 때, 더 나중에 사용되는 것을 뽑는다.
                tmp = j
                tmp_i = scheduling[scheduling_idx:].index(j)
        adaptor[adaptor.index(tmp)] = i
        tmp = tmp_i = 0
        count += 1
    scheduling_idx += 1

print(count)
