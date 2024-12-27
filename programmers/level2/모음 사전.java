import java.util.*;

class Solution {
    public String[] arr = {"A", "E", "I", "O", "U"};
    public int count = 0;
    public int num = 0;

    public int solution(String word) {
        int answer = 0;
        dfs("", word);
        answer = num;
        return answer;
    }


    public void dfs(String nowWord, String targetWord) {
        if (num == 0) {
            if (nowWord.length() > 5) {
                return;
            }
            if (nowWord.equals(targetWord)) {
                num = count;
                return;
            }
            count++;
            for (String a: arr) {
                dfs(nowWord + a, targetWord);
            }
        }

    }
}