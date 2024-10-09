def solution(id_list, report, k):
    answer = []
    reported_dict = {}
    report_list = {}

    for id in id_list:
        reported_dict[id] = 0
        report_list[id] = []

    for r in report:
        reporter, reported = r.split(" ")
        if reported not in report_list[reporter]:  # 신고를 한 경험이 없는 경우
            reported_dict[reported] += 1  # 신고 당한 횟수 증가
            report_list[reporter].append(reported)  # 신고 리스트에 삽입

    for key, value in report_list.items():  # 신고 리스트 딕셔너리 조회
        sum = 0  # 총 메일 발송 횟수 체크
        for l in value:  # 리스트 조회
            if reported_dict[l] >= k:  # 메일 전송 기준 신고 횟수보다 크거나 같은 경우
                sum += 1
        answer.append(sum)

    return answer