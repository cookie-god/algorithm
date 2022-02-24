import sys

arr = sys.stdin.readline().strip() #개행 제거
check = [0]*26 #알파벳 개수 체크

for alpha in arr:
    check[ord(alpha)-65] += 1 #알파벳 개수 카운팅

leftArr = [] #추후에 배열일 뒤집기만 하면 돼서, 왼쪽만 저장
centerCount = 0 #가운데 개수 체크
center = 'Z' #가운데값 기본값 세팅

for i in range(len(check)):
    if check[i] == 0: #알파벳 개수 0개인 경우 continue
        continue

    if centerCount > 1: #center가 여러개라면 반복문 탈출후 실패 메시지 띄움
        break

    if check[i] < 2: # 1인 경우 센터로 지정
        center = chr(i+65)
        centerCount += 1
    else:
        if check[i] % 2 == 1: #2로 나눴는데 1인 경우 센터로 지정
            center = chr(i + 65)
            centerCount += 1

        for j in range(check[i]//2): #몫만큼 왼쪽 배열에 넣음
            leftArr.append(chr(i+65))


if centerCount <= 1: #center가 있거나 하나만 있을때 출력
    leftString = ''.join(leftArr) #합치는 과정
    if centerCount == 0: #center가 없는 경우
        print(leftString + leftString[::-1])
    else: #center가 있는 경우
        print(leftString + center + leftString[::-1])
else: #center 개수가 1개보다 많으면 실패 메시지 출력
    print("I'm Sorry Hansoo")