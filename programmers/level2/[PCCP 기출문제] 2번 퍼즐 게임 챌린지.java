import java.util.*;
import java.lang.Math;

class Solution {
    public long check(int[] diffs, int[] times, long level) {
        long time = 0;

        for (int i = 0; i < diffs.length; i++) {
            if (diffs[i] <= level) {
                time += times[i];
            } else {
                int nowTime = times[i];
                int prevTime = i == 0 ? 0 : times[i-1];
                time += (nowTime + prevTime) * (diffs[i] - level) + nowTime;
            }
        }
        return time;
    }

    public long solution(int[] diffs, int[] times, long limit) {
        long answer = 0;
        long start = 0;
        long end = (long) Math.pow(10, 15);
        long mid = 0;
        long sum = 0;

        while (start <= end) {
            mid = (start + end) / 2;
            sum = check(diffs, times, mid);

            // System.out.println("start = " + start + " end = " + end + " mid = " + mid + " sum = "+ sum);

            if (sum <= limit) {
                end = mid - 1;
                answer = mid;
            } else {
                start = mid + 1;
            }
        }

        if (answer == 0) { // 모두 해결이 가능했어서 숙련도 연산이 되지 않았을 경우
            answer = 1;
        }
        return answer;
    }
}