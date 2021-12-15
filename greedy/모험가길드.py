n = int(input())
data = list(map(int, input().split()))

data.sort()
i = 0
sum = 0
result = 0

while i < n :
    sum += 1

    if sum >= data[i] :
        sum = 0
        result += 1

    i += 1

print(result)