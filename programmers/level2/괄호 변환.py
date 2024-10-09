def checkBalance(s):  # 균형잡힌 괄호 문자열의 인덱스 리턴하는 함수
    count = 0
    for i in range(len(s)):
        if s[i] == '(':
            count += 1
        else:
            count -= 1
        if count == 0:
            return i


def checkProper(s):  # 올바른 괄호 문자열인지 체크
    count = 0
    for i in s:
        if i == '(':
            count += 1
        else:
            if count == 0:  # 이미 count가 0인데 ')'라면 올바른 괄호 문자열 아님
                return False
            count -= 1
    return True


def dfs(s):  # dfs 함수
    answer = ''
    if s == '':  # p가 공백이라면
        return answer
    index = checkBalance(s)
    u = s[0:index + 1]
    v = s[index + 1:len(s)]

    if checkProper(u):
        answer = u + dfs(v)
    else:
        answer = '('
        answer += dfs(v)
        answer += ')'

        u = list(u[1:len(u) - 1])
        for i in range(len(u)):
            if u[i] == '(':
                u[i] = ')'
            else:
                u[i] = '('
        answer += "".join(u)

    return answer


def solution(p):
    return dfs(p)