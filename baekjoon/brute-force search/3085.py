import sys

def check():
    # 초기값 세팅
    answer = 1

    # 행, 열 순회를 위한 for문
    for i in range(N):
        cnt = 1
        # 열 순회하면서 연속되는 숫자 카운트
        for j in range(1, N):
            if arr[i][j] == arr[i][j-1]:
                cnt += 1
            else:
                cnt = 1
            if cnt > answer:
                answer = cnt
        cnt = 1
        # 행 순회하면서 연속되는 숫자 카운트
        for j in range(1, N):
            if arr[j][i] == arr[j-1][i]:
                cnt += 1
            else:
                cnt = 1

            if cnt > answer:
                answer = cnt
    return answer

N = int(sys.stdin.readline())
arr = []
result = 0
flag = False

for i in range(N):
    arr.append(list(map(str, sys.stdin.readline().strip())))

for i in range(N):
    for j in range(N):
        # 열 변경
        if j != N-1:
            if arr[i][j] != arr[i][j+1]:
                # 숫자 변경
                arr[i][j], arr[i][j+1] = arr[i][j+1], arr[i][j]
                result = max(result, check())
                # 복구
                arr[i][j], arr[i][j+1] = arr[i][j+1], arr[i][j]

        # 행 변경
        if i != N-1:
            if arr[i][j] != arr[i+1][j]:
                # 숫자 변경
                arr[i][j], arr[i+1][j] = arr[i+1][j], arr[i][j]
                result = max(result, check())
                # 복구
                arr[i][j], arr[i + 1][j] = arr[i + 1][j], arr[i][j]

print(result)
