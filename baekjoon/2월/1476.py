import sys

E, S, M = map(int, sys.stdin.readline().split())

i = 1 #E 비교대상
j = 1 #S 비교대상
k = 1 #M 비교대상
result = 0 #카운트
while(1):
    result += 1 #카운트 증가
    if i == E and S == j and M == k: #모두 같다면
        break
    else :
        i += 1
        j += 1
        k += 1 #증가
        if i == 16: #최대값인지
            i = 1
        if j == 29: #최대값인지
            j = 1
        if k == 20: #최대값인지
            k = 1

print(result)
