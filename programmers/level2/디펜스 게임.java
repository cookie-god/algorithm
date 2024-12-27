import java.util.*;

class Solution {
    public int solution(int n, int k, int[] enemy) {
        int answer = 0;
        PriorityQueue<Integer> pq = new PriorityQueue<>();
        int num = 0;

        for (int e: enemy) {
            if (k > 0) { // 일단 우선순위 큐에 모두 삽입
                pq.offer(e);
                k--;
            } else {
                num = pq.poll(); // 큐 추출
                if (num > e) { // 큐에 있던 적이 지금 적보다 강하다면
                    pq.offer(num); // 다시 큐에 삽입
                    n -= e; // 이번 적 처리
                } else { // 큐에 있던 적이 지금 적보다 약하다면
                    pq.offer(e); // 현재 적을 다시 큐에 삽입
                    n -= num; // 큐에 있던 적 처리
                }
            }
            if (n < 0) { // 적을 처치할 수 없었던 경우
                break;
            }
            answer++; // 처치 횟수 증가
        }

        return answer;
    }
}