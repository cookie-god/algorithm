import sys

N, K = map(int, sys.stdin.readline().split())
array = []

for i in range(N):
    array.append(int(sys.stdin.readline().strip()))

result = 0 #동전값
while True:
    N -= 1
    if K == 0: #탈출 조건
        break
    if K // array[N] > 0: #몫이 0보다 크다면
        result += K // array[N] #몫만큼 동전개수 더함
        K %= array[N] #K 최신화

print(result)
