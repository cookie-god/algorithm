import sys

N = int(sys.stdin.readline())

array = []

for i in range(N):
    array.append(int(sys.stdin.readline())) # 주어진 숫자만큼 배열 받음

count = 0 # 답
idx = 1

if N == 1: # 한개인 경우 0
    print(count)
else:
    while True:
        if array[0] > max(array[1:]): # 첫번째 인덱스 이후부터 최대값이랑 비교
            print(count)
            break
        else:
            idx = array.index(max(array[1:])) # 가장 최대값 인덱스 저장
            if idx == 0: # index 함수는 같은 값이 있으면 가장 최소의 위치 리턴, 그러나 첫번째를 0으로 하기 때문에 1 더함
                idx = 1
            array[0] += 1
            array[idx] -= 1
            count += 1
