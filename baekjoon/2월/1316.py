import sys

N = int(sys.stdin.readline()) #sys를 이용해서 입력을 더 빠르게 할 수 있음

array = [] #문자열 입력받음
result = 0 #정답
for i in range(N):
    array.append(sys.stdin.readline().strip()) #각 문자열을 주어진 개수만큼 입력 받음


for i in range(N):
    length = len(array[i]) #각 문자열의 길이를 입력 받음
    checkAlpha = [0] * 26
    firstAlpha = 0 #각 문자열에서 앞의 알파벳
    count = 0 #검사한 문자 개수 체크하는 변수
    for unit in array[i]:
        if firstAlpha == 0: #앞의 알파벳이 없는 경우
            firstAlpha = unit #앞의 알파벳 변경해줌
            checkAlpha[ord(unit)-97] += 1 #이미 사용한 문자라 표시
        else: #앞의 알파벳이 있는 경우
            if firstAlpha != unit: #앞의 알파벳과 다른경우
                if checkAlpha[ord(unit)-97] != 0: #이미 사용한 문자인 경우
                    break
                else: #이미 사용하지 않은 문자인 경우
                    checkAlpha[ord(unit)-97] += 1 #이미 사용한 문자라 표시
            firstAlpha = unit #앞의 알파벳 변경해줌
        count += 1 #검사완료 문자 개수 체크

    if count == length: #검사완료한 문자 개수와 전체 길이가 같은지 체크
        result += 1

print(result)