n = 1260
count = 0

coinType = [500, 100, 50, 10]

for coin in coinType :
    count += n // coin
    n %= coin

print(count)