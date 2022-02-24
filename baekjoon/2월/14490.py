import sys

N, M = map(int, sys.stdin.readline().strip().split(':'))

def gcd(a, b): #최대 공약수 구하는 함수
    while b > 0:
        tmp = a
        a = b
        b = tmp % b
    return a

a = gcd(N, M)
print('%d:%d' %(N // a, M // a)) #최대 공약수로 나눔