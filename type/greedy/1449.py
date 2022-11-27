import sys

N, L = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))

# 오름차순 정렬
arr.sort()

# 첫번째 지점 셋팅
start = arr[0]

# 개수 추가
count = 1

# 배열 길이
length = len(arr)

for i in range(1, length):
    # 테이프 범위 내에 물이 새는 곳이 존재한다면
    if arr[i] in range(start, start + L):
        # 테이프 그대로 사용
        continue
    else:
        # 새로운 테이프 사용, 테이프 갯수 추가
        start = arr[i]
        count += 1

print(count)