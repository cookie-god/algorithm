import sys

def dfs(depth, num, pCount, mCount, tCount, dCount):
    global maxResult, minResult
    if N == depth:  # 깊이가 N이랑 같은 경우
        maxResult = max(maxResult, num)
        minResult = min(minResult, num)
        return

    if pCount:  # 더하기가 남아있는 경우
        dfs(depth + 1, num + array[depth], pCount - 1, mCount, tCount, dCount)
    if mCount:  # 빼기가 남아있는 경우
        dfs(depth + 1, num - array[depth], pCount, mCount - 1, tCount, dCount)
    if tCount:  # 곱하기가 남아있는 경우
        dfs(depth + 1, num * array[depth], pCount, mCount, tCount - 1, dCount)
    if dCount:  # 나누기가 남아있는 경우
        dfs(depth + 1, int(num / array[depth]), pCount, mCount, tCount, dCount - 1)  # -1 // 3인 경우 0이 아닌 -1로 출력돼서 나누기에서 int로 변환


N = int(sys.stdin.readline().strip())
array = list(map(int, sys.stdin.readline().split()))
plusCount, minusCount, multiplyCount, divideCount = map(int, sys.stdin.readline().split())
maxResult = -1000000001
minResult = 1000000001

dfs(1, array[0], plusCount, minusCount, multiplyCount, divideCount)
print(maxResult)
print(minResult)