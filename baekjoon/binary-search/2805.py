import sys

def binarySearch(start, end):
    global result

    # 탈출 조건
    if start > end:
        return

    mid = (start + end) // 2  # 중간값 설정
    total = 0  # 잘린 나무의 총 길이 계산
    for item in array:
        if item >= mid:
            total += item - mid


    if total == M:  # 잘린 나무길이가 M과 정확히 일치하는 경우
        result = mid
    elif total > M:  # 잘린 나무길이가 M보다 큰 경우
        result = mid  # result에 해당 mid 값 저장. 적어도 M미터 얻어야 하기 때문
        binarySearch(mid + 1, end)  # start의 위치를 변경해줌
    else:  # 잘린 나무의 길이가 M보다 작은 경우
        binarySearch(start, mid - 1)  # end의 위치를 변경해줌

N, M = map(int, sys.stdin.readline().split())
array = list(map(int, sys.stdin.readline().split()))
result = max(array)
binarySearch(0, max(array))  # 0과 가장 긴 길이의 나무를 start와 end로 설정
print(result)
