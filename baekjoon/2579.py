import sys

n = int(sys.stdin.readline())
array = []
dp = [] #각 인덱스는 해당 인덱스까지 올라가는데 최고 값

for i in range (n):
    array.append(int(sys.stdin.readline()))

if n == 1:
    print(array[0])
else:
    dp.append(array[0]) #dp[0]은 첫번째 계단
    dp.append(max(array[0]+array[1], array[1])) #dp[1]은 첫번째와 두번째 더한것과 두번째 계단만 더한것중 큰 값
    dp.append(max(array[0]+array[2], array[1]+array[2])) #dp[2]는 첫번째와 세번째 계단 더한것과, 첫번째와 두번째 계단 더한것중 큰 값

    for i in range(3, n):
        dp.append(max(dp[i-3]+array[i-1]+array[i], dp[i-2]+array[i])) #처음 비교값은 2칸이 인접한 경우, 두번째 비교값은 한칸 떨어져있는 경우

    print(dp[n-1])