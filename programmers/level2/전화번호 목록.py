from collections import defaultdict


def solution(phone_book):
    answer = True

    phone_dict = defaultdict(int)
    for phone in phone_book:
        phone_dict[phone] = 1

    for phone in phone_book:
        for i in range(20):
            if phone[0:i] in phone_dict and phone[0:i] != phone:
                return False

    #     phone_dict = defaultdict(list)

    #     for phone in phone_book:
    #         phone_dict[len(phone)].append(phone)

    #     phone_dict = sorted(phone_dict.items(), key=lambda x:x[0])

    #     for key, value in phone_dict:
    #         for phone in phone_book:
    #             if key < len(phone):
    #                 if phone[0:key] in value:
    #                     return False

    # for phone1 in phone_book:
    #     for phone2 in phone_book:
    #         if len(phone1) > len(phone2): # 길이 체크
    #             continue
    #         if phone1 != phone2: # 다른 경우에만
    #             if phone1 == phone2[0:len(phone1)]:
    #                 return False

    # 시간 초과 코드
    # for phone1 in phone_book:
    #     for phone2 in phone_book:
    #         if phone1 != phone2: # 다른 경우에만
    #             if phone1 == phone2[0:len(phone1)]:
    #                 return False

    return answer