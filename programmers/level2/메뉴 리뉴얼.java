import java.util.*;

class Solution {
    Map<String, Integer> hashMap = new HashMap<>();
    List<String> answerList = new ArrayList<>();

    public String[] solution(String[] orders, int[] course) {
        for (int i = 0; i < orders.length; i++) {
            char[] arr = orders[i].toCharArray(); // 문자열 내 문자들 변경
            Arrays.sort(arr); // 문자 정렬
            orders[i] = String.valueOf(arr); // 문자열로 변경
        }

        for (int courseLength: course) {
            for (String order: orders) { // course 수에 맞는 조합 추출
                combination("", order, courseLength); // 각 order에 맞는 조합 추출
            }

            if (!hashMap.isEmpty()) {
                List<Integer> countList = new ArrayList<>(hashMap.values()); // map의 value만 List로 변환
                int max = Collections.max(countList); // 최대값 계산

                if (max > 1) { // 중복 메뉴가 2번 이상인 경우에만
                    for (String key: hashMap.keySet()) { // map의 key값들 순회하면서 체크
                        if (hashMap.get(key) == max) {
                            answerList.add(key);
                        }
                    }
                }
            }
            hashMap.clear(); // hashmap 초기화
        }

        Collections.sort(answerList); // 알파벳순 정렬
        String[] answer = new String[answerList.size()];
        for (int i = 0; i < answer.length; i++) {
            answer[i] = answerList.get(i);
        }

        return answer;
    }

    public void combination(String order, String others, int count) {
        if (count == 0) { // 조합 계산이 다 된 경우
            // System.out.println("order = " + order);
            hashMap.put(order, hashMap.getOrDefault(order, 0) + 1); // map에 추가
            return;
        }
        // System.out.println("check = " + order + " others = " + others);

        for (int i = 0; i < others.length(); i++) {
            // System.out.println("i = " + i + " before = " + order + " : " + others + "=>  " + count);
            combination(order + others.charAt(i), others.substring(i + 1), count - 1); // 재귀로 계산 
            // System.out.println("i = " + i + " after = " + order + " : " + others + "=>  " + count);
        }
    }
}