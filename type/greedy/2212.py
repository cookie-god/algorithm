import sys

N = int(sys.stdin.readline().strip())
K = int(sys.stdin.readline().strip())
sensor = list(map(int, sys.stdin.readline().split()))

if N <= K:  # 집중국의 개수가 더 많은 경우는 수신 가능 영역이 0
    print(0)
    sys.exit(0)

sensor.sort()  # 센서 정렬

array = []  # 각 센서의 차이 값을 저장하는 리스트
for i in range(1, N):
    array.append(sensor[i] - sensor[i-1])

array.sort(reverse=True)  # 내림차순으로 정렬

for _ in range(K - 1):  # K-1번 반복하는 이유 -> K개의 그룹을 만들기 위해서 그런 다음 가장 차이가 많이 나는 거리는 제거
    array.pop(0)

print(sum(array))