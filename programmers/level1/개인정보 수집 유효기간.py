def checkValidation(terms, item, today):
    duration = ''
    date = ''
    for term in terms:
        if item[1] == term[0]:  # 개인정보 수집가 같은 경우 찾기
            duration = term[1]
            date = item[0]
            break

    data = date.split('.')
    year = int(data[0])
    month = int(data[1])
    day = data[2]

    month += int(duration)
    if month > 12:
        year += month // 12  # 몫만큼 년도 더해주기
        month %= 12  # 나눈 나머지를 월로 설정해주기

    # 12월에서 기간이 12인 경우
    if month == 0:
        year -= 1
        month = 12

    year = str(year)
    month = '0' + str(month) if month < 10 else str(month)

    if year + '.' + month + '.' + day <= today:
        return True
    return False


def solution(today, terms, privacies):
    answer = []
    termArray = []
    for item in terms:
        termArray.append(item.split())

    privacyArray = []
    for item in privacies:
        privacyArray.append(item.split())

    idx = 0
    for item in privacyArray:
        if checkValidation(termArray, item, today):
            answer.append(idx + 1)
        idx += 1

    return answer

print(solution("2022.05.19", ["A 6", "B 12", "C 3"], ["2021.05.02 A", "2021.07.01 B", "2022.02.19 C", "2022.02.20 C"]))
print(solution("2020.01.01", ["Z 3", "D 5"], ["2019.01.01 D", "2019.11.15 Z", "2019.08.02 D", "2019.07.01 D", "2018.12.28 Z"]))
print(solution("2022.10.01", ["A 12"], ["2021.12.01 A"]))