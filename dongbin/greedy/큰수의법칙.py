n = [3, 4, 3, 4, 3]
m = 7
k = 2

answer = 0
n.sort()
length = len(n)
answer += n[length-1] * k * (m // (k+1))
answer += n[length-2] * (m // (k+1))
answer += n[length-1] * (m % (k+1))

print(answer)