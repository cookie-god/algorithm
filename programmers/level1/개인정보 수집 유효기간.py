def checkValidation(terms, item, today):
    duration = ''
    date = ''
    for term in terms:
        if item[1] == term[0]:
            duration = term[1]
            date = item[0]
            break

    data = date.split('.')
    year = int(data[0])
    month = int(data[1])
    day = data[2]

    month += int(duration)
    if month > 12:
        year += int(month // 12)
        month %= 12

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