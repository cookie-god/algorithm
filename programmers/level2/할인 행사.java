import java.util.*;

class Solution {
    public int solution(String[] want, int[] number, String[] discount) {
        int answer = 0;
        Map<String, Integer> wantMap = new HashMap<>();

        for (int i = 0; i < want.length; i++) {
            wantMap.put(want[i], number[i]);
        }

        for(int i = 0; i < discount.length; i++) {
            Map<String, Integer> discountMap = new HashMap<>();
            int end = i + 10 > discount.length ? discount.length : i + 10;
            for (int j = i; j < end; j++) {
                discountMap.put(discount[j], discountMap.getOrDefault(discount[j], 0) + 1);
            }
            if (check(wantMap, discountMap)) {
                answer += 1;
            }
        }
        return answer;
    }

    public boolean check(Map<String, Integer> wantMap, Map<String, Integer> discountMap) {
        for (Map.Entry<String, Integer> want: wantMap.entrySet()) {
            if (discountMap.containsKey(want.getKey())) {
                if (want.getValue() - discountMap.get(want.getKey()) > 0) {
                    return false;
                }
            } else {
                return false;
            }
        }
        return true;
    }
}