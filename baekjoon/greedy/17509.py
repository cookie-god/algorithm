import sys

arr = []
sum = 0
result = 0

for i in range(11):
    V, I = map(int, sys.stdin.readline().split())
    # 튜플 형태로 배열에 삽입
    arr.append((V, I))

# 첫번째 튜플 원소로 정렬
arr.sort(key=lambda x: x[0])

for item in arr:
    # 시간 추가
    sum += item[0]
    # 페널티 추가
    result += sum + item[1]*20

print(result)
