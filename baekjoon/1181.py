import sys

N = int(sys.stdin.readline()) #sys를 이용해서 입력을 더 빠르게 할 수 있음

array = []

for i in range(N):
    array.append(sys.stdin.readline()) #각 문자열을 주어진 개수만큼 입력 받음

array = set(array) #집합을 이용해서 중복값들을 제거
tmpArray = list(array) #중복값 제거된 배열을 따로 저장

tmpArray.sort() #알파벳 순서대로 정렬
tmpArray.sort(key = len) #길이가 짧은 것으로 정렬

for answer in tmpArray:
    print(answer, end='') #개행 없이 출력
