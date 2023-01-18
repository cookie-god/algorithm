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
    index = checkBalance(s)  # 균형잡힌 문자열 위치 체크
    # u, v 나눔
    u = s[0:index + 1]
    v = s[index + 1:len(s)]

    # u가 올바른 괄호 문자열인지 체크
    if checkProper(u):
        answer = u + dfs(v)  # 3-1번 수행
    else:  # 4번 수행
        answer = '('  # 4-1번 수행
        answer += dfs(v)  # 4-2번 수행
        answer += ')'  # 4-3번 수행

        u = list(u[1:len(u) - 1])  # 4-4 수행
        for i in range(len(u)):  # 4-4 수행
            if u[i] == '(':
                u[i] = ')'
            else:
                u[i] = '('
        answer += "".join(u)

    return answer  # 4-5 수행


def solution(p):
    return dfs(p)

print(solution("(()())()"))
print(solution(")("))
print(solution("()))((()"))