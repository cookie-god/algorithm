import sys

N = int(sys.stdin.readline()) #입력
result = 0

for i in range(N):
    array = sys.stdin.readline().strip() #문자열 입력
    stack = [] #선이 겹치지 않는 아치형이기 때문에 스택
    for alpha in array:
        if len(stack) != 0 and alpha == stack[-1]: #스택이 비어있지 않고, 단어가 스택의 마지막과 같은 경우 pop
            stack.pop()
        else:
            stack.append(alpha) #스택이 비어있거나 단어가 스택의 마지막과 다른 경우 push
    if len(stack) == 0: #스택이 비어있다면 좋은단어
        result += 1
print(result)