import sys

N = int(sys.stdin.readline().strip())
A = list(map(int, sys.stdin.readline().split()))
B = list(map(int, sys.stdin.readline().split()))

A.sort() #오름차순 정렬
B.sort(reverse=True) #내림차순 정렬

result = 0
for i in range(N):
    result += A[i]*B[i]

print(result)