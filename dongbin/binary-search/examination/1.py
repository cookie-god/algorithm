import sys

# 가장 첫번째 x 위치 찾는 함수
def leftBinarySearch(start, end):
  global minIdx

  # 탈출 조건
  if start > end:
    return

  mid = (start + end) // 2  # mid 값 설정

  if array[mid] > x:  # array[mid]값이 x보다 크다면 end 값을 더 낮게 변경
    leftBinarySearch(start, mid - 1)
  elif array[mid] == x:  # array[mid]값과 x가 같다면 end 값을 더 낮게 변경해서 같은 원소 있는지 체크
    minIdx = mid  # minIdx 최신화
    leftBinarySearch(start, mid - 1)
  else:  # array[mid]값이 x보다 작다면 start 값을 더 크게 변경
    leftBinarySearch(mid + 1, end)

# 가장 마지막 x 위치 찾는 함수
def rightBinarySearch(start, end):
  global maxIdx

  # 탈출 조건
  if start > end:
    return

  mid = (start + end) // 2  # mid 값 설정

  if array[mid] > x:  # array[mid]값이 x보다 크다면 end 값을 더 낮게 변경
    rightBinarySearch(start, mid - 1)
  elif array[mid] == x:  # array[mid]값과 x가 같다면 start 값을 더 크게 변경해서 같은 원소 있는지 체크
    maxIdx = mid
    rightBinarySearch(mid + 1, end)
  else:  # array[mid]값이 x보다 작다면 start 값을 더 크게 변경
    rightBinarySearch(mid + 1, end)

N, x = map(int, sys.stdin.readline().split())
array = list(map(int, sys.stdin.readline().split()))
minIdx = N  # 가장 첫번째 x 위치
maxIdx = -1  # 가장 마지막 x 위치

leftBinarySearch(0, N - 1)  # 가장 첫번째 x 위치 찾는 함수
rightBinarySearch(0, N - 1)  # 가장 마지막 x 위치 찾는 함수

if maxIdx == -1 and minIdx == N:  # x인 원소가 존재하지 않았다면 -1 출력
  print(-1)
else:
  print(maxIdx - minIdx + 1)