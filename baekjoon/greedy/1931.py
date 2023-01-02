import sys

N = int(sys.stdin.readline().strip())
arr = []

for i in range(N):
    a, b = map(int, sys.stdin.readline().split())
    arr.append((a, b))

# 회의 종료시간에 맞춰 오름차순 정렬을 하고, 그 뒤에 회의 시작시간에 맞춰 오름차순 정렬
arr.sort(key=lambda x: (x[1], x[0]))

result = 1  # 정렬된 첫번째 회의 개수
end = arr[0][1]  # 회의 종료시간 셋팅
for i in range(1, N):
    # 회의 종료시간보다 다음 회의 시간이 큰 경우
    if arr[i][0] >= end:
        result += 1  # 회의실 이용횟수 추가
        end = arr[i][1]  # 회의 종료시간 변경

print(result)
