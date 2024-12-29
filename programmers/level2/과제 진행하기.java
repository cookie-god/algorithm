import java.util.*;

class Solution {
    public List solution(String[][] plans) {
        List<Plan> planList = new ArrayList<>();
        List<String> answer = new ArrayList<>();
        Stack<Remain> stack = new Stack<>();
        int time = 0;
        int tempTime;

        for (String[] plan: plans) {
            time = makeTimeToMinutes(plan[1]);
            planList.add(new Plan(plan[0], time, time + Integer.parseInt(plan[2])));
        }

        planList.sort(Comparator.comparingInt(plan -> plan.startTime));

        for (int i = 0; i < planList.size(); i++) {
            if (i == planList.size() - 1) {
                stack.push(new Remain(planList.get(i).name, planList.get(i).endTime - planList.get(i).startTime));
                break;
            }

            if (planList.get(i).endTime <= planList.get(i+1).startTime) {
                answer.add(planList.get(i).name);
                tempTime = planList.get(i+1).startTime - planList.get(i).endTime;

                while (tempTime != 0 && stack.size() != 0) {
                    for (Remain element: stack) {
                        System.out.println(element.name + " " + element.time);
                    }
                    Remain remain = stack.pop();
                    if (remain.time <= tempTime) {
                        answer.add(remain.name);
                        tempTime -= remain.time;
                    } else {
                        stack.push(new Remain(remain.name, remain.time - tempTime));
                        tempTime = 0;
                    }
                }
            } else {
                stack.push(new Remain(planList.get(i).name, planList.get(i).endTime - planList.get(i+1).startTime));
            }
        }
        while (stack.size() > 0) {
            Remain remain = stack.pop();
            answer.add(remain.name);
        }
        return answer;
    }

    public int makeTimeToMinutes(String time) {
        String[] arr = time.split(":");
        int hour = Integer.parseInt(arr[0]);
        int minute = Integer.parseInt(arr[1]);
        return hour * 60 + minute;
    }

    public static class Plan {
        String name;
        int startTime;
        int endTime;

        public Plan(String name, int startTime, int endTime) {
            this.name = name;
            this.startTime = startTime;
            this.endTime = endTime;
        }
    }

    public static class Remain {
        String name;
        int time;

        public Remain(String name, int time) {
            this.name = name;
            this.time = time;
        }
    }
}