import sys
from collections import deque

N = int(sys.stdin.readline().strip())
array = [i+1 for i in range(N)]
queue = deque(array)
cnt = 1
n = 0

while len(queue) != 1 :
    if cnt % 2 == 0:
        queue.append(queue.popleft())
    else:
        queue.popleft()

    cnt += 1

print(queue[0])
