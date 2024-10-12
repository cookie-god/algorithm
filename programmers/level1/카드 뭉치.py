from collections import defaultdict

def solution(cards1, cards2, goal):
    answer = 'Yes'
    idx1 = 0 # card1의 현재 인덱스
    idx2 = 0 # card2의 현재 인덱스
    
    for g in goal:
        if idx1 < len(cards1) and cards1[idx1] == g: # 인덱스 검사 && 카드 내용 검사
            idx1 += 1
        elif idx2 < len(cards2) and cards2[idx2] == g: # 인덱스 검사 && 카드 내용 검사
            idx2 += 1
        else:
            answer = "No"
            break

    return answer
