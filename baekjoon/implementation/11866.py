from collections import deque

n, k = map(int, input().split())
q = deque()
answer = []

for i in range(1, n+1):
    q.append(i) #queue에 넣는과정

while q:
    for i in range(k-1): #k-1만큼 나아가고, 다시 queue에 넣음
        q.append(q.popleft())
    answer.append(q.popleft()) #정답 배열에 넣음

print("<", end="")
for i in range(len(answer)-1):
    print("%d, " %answer[i], end="")
print(answer[len(answer)-1], end="")
print(">")



