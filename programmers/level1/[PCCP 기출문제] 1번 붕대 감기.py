
def solution(bandage, health, attacks):
    maxHealth = health # 최대 체력 저장
    answer = health # 현재 체력 저장
    lastAttackSecond = 0 # 가장 최근 공격 시간


    def getHealth(result, attackSecond, damage):
        if result == -1 : # 이미 죽은 애라면 -1
            return -1

        result = result + ((attackSecond - lastAttackSecond - 1) * bandage[1]) # 공격 당한 1초 빼고 현재 초에서 가장 최근초까지의 회복량

        if (attackSecond - lastAttackSecond - 1) // bandage[0] >= 1: # 붕대 감은 적이 있다면 회복 스킬 사용
            result = result + (((attackSecond - lastAttackSecond - 1) // bandage[0]) * bandage[2])

        if result > health: # 초과한 경우 최대 체력으로 셋팅
            result = health

        result = result - damage # 공격 당하기

        if result <= 0: # 0보다 작거나 같으면 사망처리
            result = -1

        return result

    for attack in attacks:
        answer = getHealth(answer, attack[0], attack[1])
        lastAttackSecond = attack[0] # 가장 최근 공격시간 저장

    return answer