import sys

def binarySearch(start, end):
    result = 0  # 떡의 절단 길이 정하는 변수
    while start <= end:  # start가 end보다 작거나 같을 때까지
        total = 0  # 떡의 자른길이 변수
        mid = (start + end) // 2  # 중간값 저장하는 변수
        for item in array:
            if item > mid:  # item이 mid보다 크면 짤림
                total += item - mid  # 차이값 저장
        if total < M:  # 자른 떡의 총합이 M보다 작은 경우
            end = mid - 1  # 떡의 절단 마지막 위치를 mid 앞으로 위치 조정
        else:  # 자른 떡의 총합이 M보다 작거나 같은 경우
            result = mid  # 떡의 절단 길이 최신화
            start = mid + 1  # 떡의 절단 시작 위치를 mid 뒤로 위치 조정
    return result


N, M = map(int, sys.stdin.readline().split())
array = list(map(int, sys.stdin.readline().split()))

print(binarySearch(0, max(array)))  # 떡의 첫번째 길이부터 최대 길이까지 전달
