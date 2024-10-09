def solution(cap, n, deliveries, pickups):
    answer = 0
    deliveries = deliveries[::-1]  # 역순 정렬
    pickups = pickups[::-1]  # 역순 정렬
    delivery = 0  # 배달 카운팅
    pickup = 0  # 픽업 카운팅

    for i in range(n):
        delivery += deliveries[i]  # 배달해야 하는 횟수 더하기
        pickup += pickups[i]  # 픽업해야 하는 횟수 더하기

        while delivery > 0 or pickup > 0:  # 둘다 음수라면 해당 위치에 배달/픽업이 cap보다 작다는 의미이므로 가능
            delivery -= cap  # 용량 만큼 빼주기
            pickup -= cap  # 용량 만큼 빼주기
            answer += (n - i) * 2  # 현재 인덱스에서 n만큼 빼고 왕복 길이 계산

    return answer

    #     deliveryDict = {}
    #     pickupDict = {}
    #     for i in range(n-1, -1, -1):
    #         if deliveries[i] != 0:
    #             deliveryDict[i+1] = deliveries[i]
    #         if pickups[i] != 0:
    #             pickupDict[i+1] = pickups[i]

    #     while(True):
    #         if len(deliveryDict) == 0 and len(pickupDict) == 0:
    #             break
    #         deliveryCnt = 0
    #         deliveryIdx = max(deliveryDict)
    #         pickupCnt = 0
    #         pickupIdx = max(pickupDict)

    #         for key, value in deliveryDict.items():
    #             if deliveryCnt + value <= cap:
    #                 deliveryCnt = deliveryCnt + value
    #             else:
    #                 deliveryCnt = cap

    #         for key, value in pickupDict.items():
    #             if pickupCnt + value <= cap:
    #                 pickupCnt = pickupCnt + value
    #             else:
    #                 pickupCnt = cap

    #         # print(deliveryIdx, pickupIdx)
    #         # print(max(deliveryIdx, pickupIdx))
    #         answer = answer + (max(deliveryIdx, pickupIdx) * 2)

    #         for key, value in deliveryDict.items():
    #             if deliveryCnt != 0:
    #                 if value - deliveryCnt < 0:
    #                     deliveryCnt = deliveryCnt - value
    #                     deliveryDict[key] = 0
    #                     if deliveryCnt < 0:
    #                         deliveryCnt = 0
    #                 else:
    #                     value = value - deliveryCnt
    #                     deliveryDict[key] = value
    #                     deliveryCnt = 0

    #         for key, value in pickupDict.items():
    #             if pickupCnt != 0:
    #                 if value - pickupCnt < 0:
    #                     pickupCnt = pickupCnt - value
    #                     pickupDict[key] = 0
    #                     if pickupCnt < 0:
    #                         pickupCnt = 0
    #                 else:
    #                     value = value - pickupCnt
    #                     pickupDict[key] = value
    #                     pickupCnt = 0

    #         deliveryDict = {key: value for key, value in deliveryDict.items() if value != 0}
    #         pickupDict = {key: value for key, value in pickupDict.items() if value != 0}

    return answer