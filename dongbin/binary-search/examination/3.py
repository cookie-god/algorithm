import sys

N, C = map(int, sys.stdin.readline().split())
array = []
for _ in range(N):
    array.append(int(sys.stdin.readline().strip()))

array.sort()

start = 1  # 최소 거리
end = array[-1] - array[0]  # 최대 거리
result = 0  # mid값 저장하는 변수


if C == 2:  # 공유기 2대 설치 가능하면 처음과 끝 원소 차이 result에 저장
    result = array[-1] - array[0]

else:
    while start <= end:  # 이분탐색 시작
        mid = (start + end) // 2  # 간격 계산
        value = array[0]  # 맨 처음 원소에 공유기 설치
        count = 1  # 공유기 설치 가능한 위치 개수
        for i in range(1, N):  # 처음부터 끝까지 분석
            if array[i] >= value + mid:  # 공유기를 설치할 수 있는 간격인지 체크
                value = array[i]  # 공유기 설치 위치 변경
                count += 1  # 공유기 설치 가능한 위치 개수 추가

        if count >= C:  # 공유기를 C와 같거나 더 크게 설치할 수 있는 경우
            result = mid  # 우선 result에 저장
            start = mid + 1  # start를 mid + 1로 변경해서 더 높은 수의 간격이 가능한지 체크
        else:  # 공유기를 C보다 설치를 못하는 경우
            end = mid - 1  # end를 mid - 1로 변경해서 더 낮은 수의 간격이 가능한지 체크

print(result)
