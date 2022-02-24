import sys

K = int(sys.stdin.readline())

array = []

for i in range(K):
    element = int(sys.stdin.readline())
    if element != 0: #0이 아닌경우 리스트에 포함
        array.append(element) # 주어진 숫자만큼 배열 받음
    else: #0인경우 리스트의 가장 마지막 원소 제거
        array.pop() #최근 값 pop

print(sum(array))