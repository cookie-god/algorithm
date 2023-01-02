n, k = map(int, input().split())

count = 0

while n >= k :
    count += n % k
    n -= n % k
    n //= k
    count += 1

while n > 1 :
    n -= 1
    count += 1

print(count)