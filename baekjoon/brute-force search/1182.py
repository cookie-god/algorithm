import sys

N, S = map(int, sys.stdin.readline().split())
arr = list(map(int, sys.stdin.readline().split()))
cnt = 0


def check(idx, total):
    global cnt

    if idx >= N:
        return

    total += arr[idx]

    if total == S:
        cnt += 1

    # arr[idx]를 포함하는 경우
    check(idx + 1, total)
    # arr[idx]를 포함하지 않는 경우
    check(idx + 1, total - arr[idx])


check(0, 0)
print(cnt)
