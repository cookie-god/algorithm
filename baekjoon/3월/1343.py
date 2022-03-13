import sys

S = str(sys.stdin.readline().strip())
array = S.split('.') #나누기
result = [] #tmpStr담을 배열
resultStr = "" #최종 합치는 문자열
flag = 0
for divided in array:
    tmpStr = "" #하나씩 분석하면서 붙일 문자열
    length = len(divided)
    if length % 2 == 1: #홀수면 -1 출력
        flag = 1
        break
    else:
        a = length // 4
        for i in range(0, a): #몫만큼 AAAA붙임
            tmpStr += 'AAAA'
        if length % 4 != 0: #나머지가 0이 아니면 BB붙임
            tmpStr += 'BB'
        result.append(tmpStr) #정답 배열에 추가

if flag == 1:
    print("-1")
else:
    for i in range(len(result)):
        resultStr += result[i]
        if i != len(result)-1: #마지막 원소라면 .안붙임
            resultStr += "."
    print(resultStr)
