import sys

idx = 0
result = 0
while True:
    idx += 1
    L, P, V = map(int, sys.stdin.readline().split())
    if L == 0 and P == 0 and V == 0:
        break
    # 사용 가능 일수가 나머지 값들 보다 큰 경우
    if V % P < L:
        result = ((V // P) * L) + (V % P)
    # 사용 가능 일수가 나머지 값들 보다 작은 경우
    else:
        result = (V // P) * L + L

    print('Case %d: %d' % (idx, result))
