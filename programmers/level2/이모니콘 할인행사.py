from itertools import permutations, product


def solution(users, emoticons):
    answer = []
    discountRate = [10, 20, 30, 40]
    substitution = list(product(discountRate, repeat=len(emoticons)))  # 데카르트 곱으로 모든 후보 체크

    for sub in substitution:
        totalPurchaseValue = 0
        totalJoinCount = 0
        for user in users:
            purchaseValue = 0
            for idx, emoticon in enumerate(emoticons):
                if user[0] <= sub[idx]:  # 구매가 가능한 컨디션이라면
                    purchaseValue += emoticon - emoticon * sub[idx] * 0.01  # 할인율 적용하고 난 뒤 구매 비용 추가
            if purchaseValue >= user[1]:  # 유저벌 상한선 비용 이상인 경우 이모티콘 가입
                totalJoinCount += 1
            else:  # 상한선 넘지 않았으므로 전체 구매 비용 추가
                totalPurchaseValue += purchaseValue

        answer.append([totalJoinCount, totalPurchaseValue])  # 각 세일 퍼센트별 가입인원, 구매비용 배열에 삽입

    answer = sorted(answer, key=lambda x: (-x[0], -x[1]))  # 가입수에 대해서 먼저 내림차순 정렬, 그 다음 구매 비용에 대해서 내림차순 정렬

    return answer[0]