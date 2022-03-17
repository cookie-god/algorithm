import sys

N = int(sys.stdin.readline().strip())
nArray = list(map(int, sys.stdin.readline().split()))

M = int(sys.stdin.readline().strip())
mArray = list(map(int, sys.stdin.readline().split()))
flag = 0

nArray.sort() #이분 검색을 위한 정렬

for num in mArray:
    start = 0 #시작 인덱스
    end = len(nArray)-1 #마지막 인덱스
    flag = 0

    while start <= end: #시작 인덱스가 마지막 인덱스보다 작거나 같은 경우까지
        mid = (start + end) // 2 #중간값 설정
        if num == nArray[mid]: #중간값이랑 같다면 탈출
            flag = 1
            break
        elif num < nArray[mid]: #중간값보다 작으므로 마지막 인덱스 변경
            end = mid - 1
        elif num > nArray[mid]: #중간값보다 크므로 시작 인덱스 변ㄱ여
            start = mid + 1

    print(flag)
