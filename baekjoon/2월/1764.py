import sys

n, m = map(int, sys.stdin.readline().split())
noListen = []
noLook = []
for _ in range(n):
    noListen.append(sys.stdin.readline().strip())
for _ in range(m):
    noLook.append(sys.stdin.readline().strip())

answer = list(set(noListen) & set(noLook)) #교집합이용
answer.sort()
print(len(answer))
for check in answer:
    print(check)