import sys

N, K = map(int, sys.stdin.readline().split())
arr = []
result = 0  # 동전 개수
total = K  # 연산에 사용되는 총 금액

for i in range(N):
    arr.append(int(sys.stdin.readline().strip()))

# 내림차순으로 정렬 변경
arr.sort(reverse=True)

for i in range(N):
    # 만약 주어진 동전이 총 금액보다 크다면 스킵
    if arr[i] > total:
        continue

    result += total // arr[i]  # 동전 개수 나누기 연산의 몫을 통해서 구하기
    total %= arr[i]  # 남은 금액 나머지 연산을 통해서 구하기

    # 이미 남은 금액이 0원이라면 반복문 탈출
    if total == 0:
        break

print(result)
