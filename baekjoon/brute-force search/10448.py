import sys

def check(num):
    for i in range(1, 45):
        for j in range(1, 45):
            for k in range(1, 45):
                if arr[i] + arr[j] + arr[k] == num:
                    return 1

    return 0


T = int(sys.stdin.readline())
arr = []

for i in range(45):
    arr.append(i * (i + 1) / 2)

for i in range(T):
    K = int(sys.stdin.readline())
    print(check(K))