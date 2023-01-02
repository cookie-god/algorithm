def solution(s):
    answer = 0
    sLen = len(s)  # 문자열 전체 길이 저장
    minValue = sLen  # 초기 최소값은 문자열 전체 길이

    criteria = 0  # 기준값
    if sLen % 2 == 1:  # 홀수인 경우 가운데 위치는 2를 나눈 몫에서 1을 더해야함
        criteria = sLen // 2 + 1
    else:
        criteria = sLen // 2

    for i in range(1, criteria + 1):  # 1 ~ 절반 길이까지로 나눠서 비교
        sameStrCount = 1  # 초기 같은 문자열의 개수
        criteriaStr = s[0:i]  # 첫번째 기준 문자열
        compressed = ''  # 반복된 문자열 적용해서 저장하는 변수
        for j in range(i, sLen, i):  # i부터 전체 길이까지 i만큼 증가하면서 반복문 진행
            if criteriaStr == s[j:j + i]:  # 기준 문자열과 부분 문자열 비교해서 같은 경우
                sameStrCount += 1  # 같은 문자열 개수를 저장하는 변수 1 더해줌
            else:  # 반복 문자열과 부분 문자열 비교해서 다른 경우
                if sameStrCount > 1:  # 같은 문자열 개수가 1보다 큰 경우
                    compressed += str(sameStrCount) + criteriaStr  # 숫자 포함해서 문자 연결
                else:  # 같은 문자열 개수가 1보다 작거나 같은 경우
                    compressed += criteriaStr  # 문자만 연결
                criteriaStr = s[j:j + i]  # 기준 문자열 최신화
                sameStrCount = 1  # 개수 최신화

        # 마지막 로직 체크
        if sameStrCount > 1:  # 같은 문자열 개수가 1보다 큰 경우
            compressed += str(sameStrCount) + criteriaStr  # 숫자 포함해서 문자 연결
        else:  # 같은 문자열 개수가 1보다 작거나 같은 경우
            compressed += criteriaStr  # 문자만 연결
        minValue = min(len(compressed), minValue)  # 최솟값 저장

    answer = minValue  # 최솟값 answer 변수에 저장
    return answer