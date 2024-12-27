import java.util.*;
import java.util.stream.Collectors;

class Solution {
    public int solution(int k, int[] tangerine) {
        int answer = 0;

        Map<Integer, Integer> counter = new HashMap<>();
        for (int t: tangerine) {
            counter.put(t, counter.getOrDefault(t, 0) + 1);
        }

        List<Map.Entry<Integer, Integer>> sortedList = counter.entrySet()
            .stream()
            .sorted((e1, e2) -> e2.getValue().compareTo(e1.getValue()))
            .collect(Collectors.toList());

        for (Map.Entry<Integer, Integer> entry : sortedList) {
            k -= entry.getValue();
            answer += 1;
            if (k <= 0) {
                break;
            }
        }

        return answer;
    }
}