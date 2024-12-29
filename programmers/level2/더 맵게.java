import java.util.*;


class Solution {
    public int solution(int[] scoville, int K) {
        int answer = 0;

        PriorityQueue<Integer> pq = new PriorityQueue<>();

        for (int s: scoville) {
            pq.offer(s);
        }

        int num = 0;
        while (!pq.isEmpty()) {
            num = pq.poll();
            if (num < K) {
                if (pq.isEmpty()) {
                    answer = -1;
                    break;
                } else {
                    pq.offer(num + (pq.poll() * 2));
                    answer++;
                }
            } else {
                break;
            }
        }
        return answer;
    }
}