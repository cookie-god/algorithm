import sys

str = sys.stdin.readline()
strLength = len(str) #총 길이
startIdx = 0 #숫자 위치 표현을 위한 인덱스값
plusValue = 0 #더하는 값
minusValue = 0 #빼는 값
plusStartFlag = 0 #첫 덧셈이 나왔는지 체크하는 플래그
minusStartFlag = 0 #첫 뺄셈이 나왔는지 체크하는 플래그
idx = 0 #인덱스
while True:
    idx += 1 #인덱스 하나씩 검사
    if idx >= strLength: #탈출 조건
        break

    if idx == strLength-1: #마지막 숫자에 대해서 int로 변경해서 덧셈값으로 설정
        plusValue += int(str[startIdx:strLength])
        break

    if str[idx] == '+': #덧셈인 경우는 무조건 덧셈값으로 설정
        plusValue += int(str[startIdx:idx])
        startIdx = idx + 1 #숫자위치 변경

    elif str[idx] == '-': #뺄셈인 경우
        if minusStartFlag == 0: #마이너스가 첫번째로 나온경우 덧셈값으로 빼기 위한 변수
            minusStartFlag = 1
            plusValue += int(str[startIdx:idx]) #덧셈값으로 추가
            startIdx = idx + 1 #숫자위치 변경

        while True: #마이너스인 그리디하게 접근을 위한 반복문
            idx += 1 #인덱스값 변경
            if idx >= strLength: #탈출 조건
                break
            if idx == strLength - 1: #마지막 숫자에 대해서 int로 변경해서 마이너스 값으로 설정
                minusValue += int(str[startIdx:strLength])
            if str[idx] == '-': #또 마이너스가 나오는 경우 마이너스 값에 추가한 뒤 탈출
                minusValue += int(str[startIdx:idx])
                startIdx = idx + 1 #숫자위치 변경
                idx -= 1 #29번째 라인인 -에 다시 접근하기 위해 idx 빼줌
                break
            elif str[idx] == '+': #플러스가 나온경우 마이너스값에 추가한 뒤 반복문 진행
                minusValue += int(str[startIdx:idx])
                startIdx = idx + 1 #숫자위치 변경

print(plusValue-minusValue)