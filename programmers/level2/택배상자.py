from collections import deque

def solution(order):
    answer = 0
    stack = deque() # 스택 -> 보조 컨테이너 벨트
    now = 1 # 현재 택배 순번
    
    for o in order:
        while now < o: # o보다 작은 택배들 모두 보조 컨테이너 벨트로 이동
            stack.append(now) # 보조 컨테이너 벨트로 이동
            now += 1 # 현재 택배 순번 증가
        
        if now == o: # now를 o만큼 이동 시켰으니 가능
            answer += 1 # 트럭에 상차 성공
            now += 1 # now위치 증가
            continue # 다음 order 확인
            
        if stack.pop() == o: # 보조 컨테이너 벨트의 마지막이 o와 같다면
            answer += 1 # 트럭에 상차 성공
            continue # 다음 order 확인
            
        break # 메인 컨테이너 벨트와 보조 컨테이너 벨트 모두 해당 못했으므로 탈출
                    
    return answer
