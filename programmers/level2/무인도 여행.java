import java.util.*;

class Solution {
    public boolean[][] visited;
    public int[] dx = {-1, 1, 0, 0};
    public int[] dy = {0, 0, -1, 1};
    public List<Integer> answerList = new ArrayList<>();
    public int row;
    public int column;

    public List solution(String[] maps) {
        row = maps.length;
        column = maps[0].length();
        visited = new boolean[row][column];

        for (int i = 0; i < row; i++) {
            for (int j = 0; j < column; j++) {
                if (maps[i].charAt(j) != 'X' && visited[i][j] == false) {
                    bfs(i, j, maps);
                }
            }
        }

        if (answerList.isEmpty()) {
            answerList.add(-1);
        }

        Collections.sort(answerList);
        return answerList;
    }

    public void bfs(int x, int y, String[] maps) {
        visited[x][y] = true;
        Queue<Pair> queue = new LinkedList<>();
        queue.offer(new Pair(x, y));
        int size = maps[x].charAt(y) - '0';
        // System.out.println(" size = " + size);

        while (queue.size() > 0) {
            Pair pair = queue.poll();
            for (int i = 0; i < 4; i++) {
                int nx = pair.x + dx[i];
                int ny = pair.y + dy[i];

                if (checkBorder(nx, ny)) {
                    if (maps[nx].charAt(ny) != 'X' && visited[nx][ny] == false) {
                        visited[nx][ny] = true;
                        queue.offer(new Pair(nx, ny));
                        // System.out.println("nx = " + nx + " ny = " + ny + " maps[nx][ny] = " + maps[nx].charAt(ny) + " size = " + size);
                        size += maps[nx].charAt(ny) - '0';
                    }
                }
            }
        }
        answerList.add(size);
    }

    public boolean checkBorder(int x, int y) {
        if (x < 0 || x >= row || y < 0 || y >= column) {
            return false;
        }
        return true;
    }

    public static class Pair {
        int x;
        int y;

        public Pair(int x, int y) {
            this.x = x;
            this.y = y;
        }
    }
}