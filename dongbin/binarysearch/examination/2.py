import sys

def binarySearch(start, end):
    global result

    # 탈출 조건
    if start > end:
        return

    mid = (start + end) // 2  # mid 값 계산

    if array[mid] == mid:  # 인덱스와 원소가 같다면
        result = mid
    elif array[mid] < mid:  # 원소가 인덱스보다 작다면 start 값 변경
        binarySearch(mid + 1, end)
    else:  # 원소가 인덱스보다 크다면 end 값 변경
        binarySearch(start, mid - 1)


N = int(sys.stdin.readline().strip())
array = list(map(int, sys.stdin.readline().split()))
result = -1  # 정답 저장하는 변수

binarySearch(0, N - 1)
print(result)