from collections import Counter


def solution(lottos, win_nums):
    answer = []

    zeroCount = 0  # 0의 개수
    correctCount = 0  # 맞춘 숫자 개수

    lottoCounter = Counter(lottos)
    winCounter = Counter(win_nums)
    zeroCount = lottoCounter[0]  # 0의 개수

    for key, value in lottoCounter.items():
        if key in winCounter and key != 0:  # 일치하는 숫자가 있고 0이 아닌 경우
            correctCount += 1

    maxCorrectCount = correctCount + zeroCount  # 최대 맞춘 개수
    if maxCorrectCount > 6:  # 6이 넘어가면 6으로 셋팅
        maxCorrectCount = 6
    minZeroCount = correctCount  # 최소 맞춘 개수

    if maxCorrectCount == 0:  # 하나도 못맞추면 6등
        answer.append(6)
    else:  # 그 외 등수에 대해선 순위 처리
        answer.append(6 - maxCorrectCount + 1)

    if minZeroCount == 0:  # 하나도 못맞추면 6등
        answer.append(6)
    else:  # 그 외 등수에 대해선 순위 처리
        answer.append(6 - minZeroCount + 1)

    return answer