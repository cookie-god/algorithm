def solution(word):
    global answer
    answer = 0
    charList = ["A", "E", "I", "O", "U"]  # 단어 리스트
    global answerFlag
    answerFlag = False  # 정답 유무 체크 플래그

    def dfs(check):
        global answerFlag
        global answer

        if len(check) > 5:  # 길이가 5를 넘는 경우 break
            return

        if answerFlag == True:  # 이미 정답을 찾은 경우
            return

        if check == word:  # 정답이라면 종료되도록
            answerFlag = True
            return

        answer += 1  # 횟수 추가
        for character in charList:
            dfs(check + character)  # 다음 문자 결합한 다음 재귀

    dfs("")
    return answer