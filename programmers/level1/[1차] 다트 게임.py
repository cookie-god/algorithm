def solution(dartResult):
    answer = 0

    idx = 0  # 문자열 위치
    num = 0  # 현재 숫자
    beforeNum = 0  # 이전 숫자
    while True:
        if idx == len(dartResult):  # 탈출 조건
            break

        if "0" <= dartResult[idx] <= "9":  # 숫자인 경우
            num = dartResult[idx]  # 숫자 저장
            if idx < len(dartResult) - 1:  # 가장 마지막 문자열이 아닌 경우에만 조사
                if num == "1" and dartResult[idx + 1] == "0":  # 1이고 뒷 자리가 0일때는 10으로 변경
                    num = "10"
                    idx += 1
            num = int(num)  # 숫자로 변환
        elif dartResult[idx] == "*" or dartResult[idx] == "#":  # 옵션인 경우
            if dartResult[idx] == "*":  # *인 경우 이전 답변에 들어갔던 beforeNum에 대해서도 처리
                num = num * 2
                answer -= beforeNum
                answer += beforeNum * 2 + num
                beforeNum = num  # 이전 숫자 저장
            else:
                num = num * -1
                answer += num
                beforeNum = num  # 이전 숫자 저장
        else:
            if dartResult[idx] == "S":  # 연산
                num = num ** 1
            elif dartResult[idx] == "D":  # 연산
                num = num ** 2
            else:  # 연산
                num = num ** 3

            if idx < len(dartResult) - 1:  # 가장 마지막 문자열이 아닌 경우
                if "0" <= dartResult[idx + 1] <= "9":  # 옵션이 없는 경우, 계산 완료
                    answer += num  # 현재 답변 저장
                    beforeNum = num  # 이전 답변 저장 *에 쓰일 수 있으니
            else:  # 가장 마지막 문자열인 경우
                answer += num  # 현재 답변 저장
                beforeNum = num  # 이전 답변 저장 -> 사실 의미 없음

        # print("===answer===")
        # print(dartResult[idx], answer)
        # print("===num===")
        # print(dartResult[idx], num)

        idx += 1

    return answer